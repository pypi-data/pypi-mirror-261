import json
import time
import traceback
from typing import Dict, List, Optional

import networkx as nx  # type: ignore

from sb_models.logger import log
from sb_models.graph.edge import EdgesProcessor
from sb_models.graph.node import Node
from sb_models.types.request import SubstrateRequest
from sb_models.graph.graph_result import GraphResult
from sb_models.graph.server_future import ServerFuture
from sb_models.substratecore.coregraph import CoreGraph
from sb_models.graph.find_futures_server import find_futures_server
from sb_models.substratecore.base_future import BaseFuture, TraceDirective, ConcatDirective


class ServerGraph(CoreGraph):
    max_concurrent = 50

    def __init__(self, futures=None, **kwargs):
        super().__init__(**kwargs)
        if futures is None:
            futures = []
        self._futures = futures

    def is_path(self):
        topo_sort = list(nx.topological_sort(self.DAG))
        return nx.is_simple_path(self.DAG, topo_sort)

    @property
    def futures(self) -> List[BaseFuture]:
        return self._futures

    @classmethod
    def from_dict(cls, graph_dict):
        id = graph_dict.get("id")
        nodes = graph_dict["nodes"]
        edges = graph_dict["edges"]
        futures = graph_dict.get("futures", [])
        futures_by_id: Dict[str, ServerFuture] = {f["id"]: ServerFuture.from_dict(f) for f in futures}
        server_futures = list(futures_by_id.values())

        G = cls(id=id, futures=server_futures, **graph_dict["initial_args"])

        for node_dict in nodes:
            node = Node.from_dict(node_dict)
            future_ids = find_futures_server(node.args)
            node.futures_from_args = [futures_by_id[fid] for fid in future_ids]
            G.add_node(node)
        repr_nodes = {n.id: n for n in G.DAG.nodes()}
        for u, v, d in edges:
            from_node = repr_nodes[u]
            to_node = repr_nodes[v]
            G.DAG.add_edge(from_node, to_node, **d)
        return G

    @staticmethod
    async def execute_node(
        n,
        fn_args,
        result,
        inferred_output,
        verbose,
        req: Optional[SubstrateRequest] = None,
    ):
        t0 = time.time()
        if verbose:
            log.info(f"RUN NODE: {n} >> {fn_args}")
        # noinspection PyProtectedMember
        loc, glob, usage = await n._run(req=req, **fn_args)
        result.set_local(n, loc)
        if glob:
            result.set_global(n, glob)
        if n == inferred_output:
            result.set_global(n, loc)
        if usage:
            result.usage[n] = usage
        if verbose:
            log.info(f"FINISH NODE ({time.time() - t0:.2f}s): {n}")
            log.info(f"    OUT:  {result.locals[n]}")
            if glob:
                log.info(f"    GLOB: {result.globals[n]}")
            if usage:
                log.info(f"    USAGE: {result.usage[n]}")

    def get_forward_args(self, n: "Node", result: "GraphResult", roots: set[str]):
        """
        Get the arguments for a node about to be run. If the node is a root node, then use initial_args from the graph.
        Otherwise, we have to find out how to take the aggregated graph results so far, and pass them to the node
        based on the edges/adapters coming into it.

        Whatever comes out of this will be passed directly to the next node as kwargs, so it must be a perfect
        fit for the next node's input signature.
        """
        node_kwargs = {}

        is_root = n.id in roots
        if is_root:
            node_kwargs.update(self.initial_args)
            node_kwargs.update(self.DAG.nodes[n])
        else:
            node_kwargs.update(self.DAG.nodes[n])

            # NB: if there are any futures in the node args, use the futures processor
            args = EdgesProcessor(self, n, result).resolve_args(use_futures=self.has_futures())
            node_kwargs.update(args)

        return node_kwargs

    def _make_implicit_dag(self) -> nx.DiGraph:
        """
        Creating the implicit DAG amounts to going through a graph and creating a dependency structure that is
        implied by the graph's future structure.

        A Future's immediately dependent node set is either the future's origin node (in the case of a traced future)
        or the set of nodes found by walking down a concat directive future items tree until we find the earliest
        future that is attached to a concrete origin node. Effectively it is finding the leaf set of the concat item
        tree after pruning the tree such that any path to a leaf terminates at the first traced node.

        There are two main ways to establish a dependency between nodes in the graph:

        1. If a future is used directly in the argument space of a node, then the node depends on the future's dependent
              node set.
        2. If a future is used in the op_stack of another future, then the future depends on the future's dependent node set.
        """

        implicit_dag = nx.DiGraph()
        futures_by_id: Dict[str, BaseFuture] = {f.id: f for f in self.futures}

        def insert_edge(f, to_node_id):
            if isinstance(f.directive, TraceDirective) and f.directive.origin_node_id:
                implicit_dag.add_edge(f.directive.origin_node_id, to_node_id)
            elif isinstance(f.directive, ConcatDirective):
                for item in f.directive.items:
                    sf = futures_by_id[item.future_id] if item.future_id else None
                    if sf:
                        insert_edge(sf, to_node_id)

        # For each node, go through the argument futures and draw dependency edges
        for n in self.DAG.nodes():
            for f in n.futures_from_args:
                insert_edge(f, n.id)

        # For each future attached to a node, go through the op_stack and draw dependency edges
        # from the sub-futures to the destination node
        for f in self.futures:
            f_origin_node_id = f.directive.origin_node_id if isinstance(f.directive, TraceDirective) else None
            if f_origin_node_id:
                for op in f.directive.op_stack:
                    if op.future_id:
                        sub_future = futures_by_id[op.future_id]
                        insert_edge(sub_future, f_origin_node_id)

        return implicit_dag

    def _inferred_output(self):
        """
        If the graph is a single path, and no nodes have output() specified, then the last node
        should be the auto output node.
        """
        is_single_path = self.is_path()
        if is_single_path:
            has_outputs_specified = False
            for n in nx.topological_sort(self.DAG):
                # noinspection PyProtectedMember
                if n._should_output_globally:
                    has_outputs_specified = True
                    break
            return None if has_outputs_specified else list(self.DAG.nodes())[-1]
        return None

    async def run(
        self,
        verbose=False,
        req: Optional[SubstrateRequest] = None,
    ) -> GraphResult:
        """
        Run the graph. The main idea here is that we have a dependency structure, either explicit (nodes and edges have been manually added)
        or implicit (nodes and edges are inferred from the future_list). In either case it is here that we come up with
        a scheduling plan for figuring out what we can run up front, and then, when any node finishes, what we can run next, if any.

        Overall the plan is to:
        1. Validate the graph
        2. Infer an output node if it's not specified
        3. Create an implicit graph from the future_list if it applies
        4. Create a dependency count for each node based on a merged view of the explicit and implicit graphs
        5. Create an async queue of tasks to run
        6. Work off the queue by scheduling anything with no unmet dependencies
            - When something finishes, update its downstream unmet dependency counts
            - If any of those counts reach 0, schedule them
        7. Collect and return the results

        """
        import asyncio

        if verbose:
            log.info("\nRUN GRAPH")
            self.network_text()

        self._check_dag()
        result = GraphResult()

        # todo(rob) think about how this should work in the implicit future case
        inferred_output_node = self._inferred_output()
        implicit_dag = self._make_implicit_dag()

        unmet_dep_counts: Dict[str, int] = {}
        out_edges_by_node: Dict[str, List[str]] = {}
        computed_roots = set()

        for n in self.DAG.nodes():
            # gather things that n depends on
            node_id = n.id
            explicit_incoming_ids = [(u.id, v.id) for u, v in self.DAG.in_edges(n)]
            implicit_incoming_ids = list(implicit_dag.in_edges(n.id))
            incoming_ids = set([u for u, _ in explicit_incoming_ids + implicit_incoming_ids])
            unmet_dep_counts[node_id] = len(incoming_ids)
            if unmet_dep_counts[node_id] == 0:
                computed_roots.add(node_id)

            # gather things that are dependent on n
            explicit_outgoing_ids = [(u.id, v.id) for u, v in self.DAG.out_edges(n)]
            implicit_outgoing_ids = list(implicit_dag.out_edges(n.id))
            outgoing = set([v for _, v in explicit_outgoing_ids + implicit_outgoing_ids])
            out_edges_by_node[node_id] = list(outgoing)

        task_queue = asyncio.Queue()

        async def execute_and_schedule(u_node, u_node_args):
            """
            Run u_node, then find all of u_node's downstream nodes and schedule them if their unmet_dep_counts reach 0
            """

            # Run u_node
            await ServerGraph.execute_node(
                u_node,
                u_node_args,
                result=result,
                inferred_output=inferred_output_node,
                verbose=verbose,
                req=req,
            )

            # Decrement unmet_dep_counts for all downstream nodes, and schedule them if they reach 0
            for v_id in out_edges_by_node[u_node.id]:
                unmet_dep_counts[v_id] -= 1
                # TODO(rob) prevent double scheduling
                if unmet_dep_counts[v_id] == 0:
                    v_node = next((u for u in self.DAG.nodes() if u.id == v_id), None)
                    if v_node:
                        next_args = self.get_forward_args(v_node, result, computed_roots)
                        await task_queue.put((v_node, next_args))
                    else:
                        log.error(f"expected to find node with id {v_id}, but did not")

        async def worker():
            while True:
                node_to_run, rn_args = await task_queue.get()
                try:
                    await execute_and_schedule(node_to_run, rn_args)
                    task_queue.task_done()
                except Exception as e:
                    log.error(f"Error in worker: {e}")
                    traceback.print_exc()
                    task_queue.task_done()

        # Start by scheduling all nodes with no unmet dependencies
        for node in self.DAG.nodes():
            if unmet_dep_counts[node.id] == 0:
                fn_args = self.get_forward_args(node, result, computed_roots)
                await task_queue.put((node, fn_args))

        workers = [asyncio.create_task(worker()) for _ in range(ServerGraph.max_concurrent)]

        await task_queue.join()

        # TODO(rob) think about how best to handle this. if raising any exception,
        #  we should consider polling and cancelling early
        exceptions = [task.exception() for task in workers if task.done() and task.exception() is not None]

        for worker in workers:
            worker.cancel()

        if exceptions:
            raise exceptions[0]

        if verbose:
            log.info(f"\nRESULT:\n{result.globals}")
        return result

    def network_text(self):
        return nx.write_network_text(self.DAG)

    def to_dict(self) -> Dict:
        as_dict = {
            "nodes": [n.to_dict() for n in self.DAG.nodes()],
            "edges": [(u.id, v.id, d) for u, v, d in list(self.DAG.edges.data())],
            "initial_args": self.initial_args,
            "futures": [f.to_dict() for f in self.futures],
            "id": self.id,
        }
        return json.loads(json.dumps(as_dict))
