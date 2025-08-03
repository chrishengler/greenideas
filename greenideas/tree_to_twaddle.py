from greenideas.pos_node import POSNode


def convert_tree(tree) -> str:
    if isinstance(tree, POSNode):
        return tree.resolve()
    else:
        raise ValueError("Tree must be a POSNode")
