class POSNode:
    def __init__(self, type_, children=None, value=None):
        self.type = type_
        self.children = children or []
        self.value = value

    def resolve(self):
        # If terminal, return the twaddle tag or value
        if self.type.twaddle_name:
            return f"<{self.type.twaddle_name}>"
        if self.value is not None:
            return str(self.value)
        # Otherwise, recursively resolve children
        return " ".join(child.resolve() for child in self.children)
