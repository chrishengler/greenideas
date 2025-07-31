class GrammarRule:
    def __init__(self, lhs, rhs, weight=1.0):
        self.lhs = lhs  # POSType
        self.rhs = rhs  # list of POSType or str (for terminals)
        self.weight = weight
