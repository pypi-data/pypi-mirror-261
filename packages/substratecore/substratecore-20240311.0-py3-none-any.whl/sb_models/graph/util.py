from typing import Dict


def node_instance(from_dict: Dict):
    from sb_models.graph.node import Node
    from sb_models.graph.modal_nodes import ModalNode
    from sb_models.graph.public_nodes import ALL_PUBLIC_NODES

    extra_args = from_dict.get("extra_args", {})

    modal_model_name = extra_args.get("model")

    public_node_key = from_dict.get("node")
    PublicNodeKlass = ALL_PUBLIC_NODES.get(public_node_key)

    if PublicNodeKlass:
        return PublicNodeKlass(**from_dict["args"])
    elif modal_model_name:
        # LEGACY nodes use `extra_args.model`
        return ModalNode(**extra_args, **from_dict["args"])
    else:
        return Node(**from_dict["args"])
