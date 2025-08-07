from greenideas.rules.grammar_rule import GrammarRule


class GrammarRuleset:
    def __init__(self):
        self.rules = list()

    def add(self, rule: GrammarRule):
        self.rules.append(rule)

    def add_rules(self, rules: list[GrammarRule]):
        for rule in rules:
            self.add(rule)
