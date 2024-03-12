## The Substrate Graph Interface

The graph interface is the primary entrypoint for describing inference 
pipelines in Substrate. At its core it is a DAG (directed acyclic graph) where nodes represent
functions, and edges carry arguments.

#### Nodes
The main node type is a `ModelNode`, which is a node that directly maps
to an entrypoint function that performs inference for a Substrate model,
e.g. `SDXL.generate` or `CLIP.embed_texts`. Another prominent node type
is `PythonNode`, which has attributes around a python runtime user-supplied
code, which will be run in a remote sandbox environment and passed on. 

Every node implements an abstract `run` method to do its job.

Over time other utility node types will be added (`Map/MultiprocessingNode`,
`ConditionalNode`, etc). The goal is to allow complete pipelines to be
specified and serialized from a client and then parsed and executed in 
our network. 

Nodes have `attributes` which will eventually be used in its `run` method
along with any `parameters` passed in from incoming edges. In general
`parameters` are a subset of `attributes`; the former can be thought of
as a "public" interface, and the latter "private" or "static" attributes
used for a node's implementation. A close analogy might be that `parameters`
are a React component's dynamic props and `attributes` are something 
like internal state and static/default props. 

#### Edges

Directed edges connect a graph, and relate a source node's output to 
a destination node's input. For analysis and scheduling, we require 
all graphs to be acyclic. Formally edges are only three pieces of information:
a `source` node reference, a `destination` node reference, and `data` that 
is communicated between the two. We should aspire to have strong typing
between node i/o and edge data so that we can validate graphs during
compilation vs. having incompatibilities show up at runtime.

#### Adapters

Nodes in the substrate graph have heterogeneous input and output interfaces
so in order to properly relate one's input to another's output, we introduce
the concept of "adapters". Adapters are directives that specify how to map
one type to another. As of now, Adapters are not arbitrary code, but instead
references to native utilities that we formalize and expose to users. Because
of this, adapters are chainable, and can roughly be thought of as lightweight
"subgraph" computations that generally transform Outputs to Inputs, or Outputs
to Final Outputs.

There is overlap here between adapters and custom code nodes, but adapters 
should feel more lightweight, more first-class, and more portable. In either
case users should be able to modularize either their adapter chains or 
adapter code nodes and easily plug them into their pipelines.

#### Outputs

While nodes have their local input and output interfaces, there also 
exists a global `GraphOutput`, which encapsulates all the information 
that a user is interested in receiving back from a graph run. For "single 
path" graphs (i.e. a straight pipeline) we automatically designate the last 
leaf node as the graph output. If a user wants more control, any node can 
be designated as a graph output. All global outputs will be collected 
during a graph's runtime and returned at the end, keyed by node.

#### Features / Principles

The high level goal is to provide an interface to developers to describe
execution graphs, and while doing so, allow our managed system to execute 
those graphs efficiently and at scale. To this end, there might be guiding 
principles for how we make decisions when it comes to the design of the 
graph. There are many examples of good/effective tools for graph composition
or execution (Airflow, MAX/MSP, Houdini, Dask, Excel, Haskell, RX, Terraform) 
which all have their own goals, design choices; we should pull inspiration
when it makes sense for us.

  - Flexibility
    - Users should be able to use this to do anything involving inference
    - Each graph should be a semantically meaningful "module" with well-defined I/O
  - Legibility
    - Ideally graphs help in both creating and understanding complex flows
  - Efficiency
    - Graphs should allow us to do formal analyses that let us schedule runs efficiently
  - Portability 
    - Should approach the serialization similar to designing a file format
    - Created primarily via SDKs in multiple programming languages
      - Can be helpful to lean on language features, but not too much