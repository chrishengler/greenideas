from greenideas.exceptions import RuleNotFoundError


class GrammarEngine:
    def __init__(self):
        self.rules = {}

    def add_rule(self, rule_name, rule_definition):
        if rule_name in self.rules:
            self.rules[rule_name].append(rule_definition)
        else:
            self.rules[rule_name] = [rule_definition]

    def generate_tree(self, start_symbol):
        if not self.rules or start_symbol not in self.rules:
            raise RuleNotFoundError(f"Rule '{start_symbol}' not found.")
        return self._expand_to_tree(start_symbol)

    def _expand_to_tree(self, symbol):
        if symbol not in self.rules:
            return symbol
        # For now just use the first
        expansion = self.rules[symbol][0]
        children = []
        for elem in expansion:
            if elem in self.rules:
                children.append(self._expand_to_tree(elem))
            else:
                children.append(elem)
        return {symbol: children}
