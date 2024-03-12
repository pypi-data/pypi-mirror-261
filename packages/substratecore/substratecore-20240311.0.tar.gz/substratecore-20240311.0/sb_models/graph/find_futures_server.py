from typing import Any, Dict, List

from sb_models.substratecore.base_future import FUTURE_ID_PLACEHOLDER


def find_futures_server(node_args: Dict) -> List[str]:
    """
    Recursively follow a node's arg tree and return all dependent Future ids in a list.
    See `EdgesProcessor.get_args_with_futures` for how `Node.futures_from_args` is used.
    See `substratecore/find_futures_client.py` for a similar client-side function.
    """

    def _find(subtree: Any) -> List[str]:
        future_ids = []
        if isinstance(subtree, dict):
            for _, val in subtree.items():
                if isinstance(val, dict) and FUTURE_ID_PLACEHOLDER in val:
                    future_ids.append(val[FUTURE_ID_PLACEHOLDER])
                else:
                    future_ids.extend(_find(val))
        elif isinstance(subtree, list):
            for item in subtree:
                future_ids.extend(_find(item))
        return future_ids

    return _find(node_args)
