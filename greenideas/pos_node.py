class POSNode:
    def __init__(self, type_, children=None, value=None):
        self.type = type_
        self.children = children or []
        self.value = value
        self.attributes = {}

    def __str__(self):
        children = (
            f"[{", ".join(str(child) for child in self.children)}]"
            if self.children
            else None
        )
        return f"{self.type.name}{children if children else ""}"

    def resolve(self):
        # If terminal, return the twaddle tag or value
        if self.type.twaddle_name:
            return f"<{self.type.twaddle_name}>"
        if self.value is not None:
            return str(self.value)
        # Otherwise, recursively resolve children
        return " ".join(child.resolve() for child in self.children)
