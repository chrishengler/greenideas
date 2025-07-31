from greenideas.grammar_rule import GrammarRule


class Grammar:
    def __init__(self):
        self.rules = {}  # {POSType: [GrammarRule, ...]}

    def add_rule(self, lhs, rhs, weight=1.0):
        rule = GrammarRule(lhs, rhs, weight)
        if lhs in self.rules:
            self.rules[lhs].append(rule)
        else:
            self.rules[lhs] = [rule]

    def get_rules(self, lhs):
        return self.rules.get(lhs, [])

    def has_rule(self, lhs):
        return lhs in self.rules
