from greenideas.pos_node import POSNode


class TreeToTwaddle:
    def convert_tree(self, tree):
        # Accepts a POSNode or dict
        if isinstance(tree, POSNode):
            return tree.resolve()
        else:
            raise ValueError("Tree must be a POSNode")
