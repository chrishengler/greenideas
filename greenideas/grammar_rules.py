from greenideas.exceptions import RuleNotFoundError
from greenideas.pos_types import POSType


class GrammarRules:
    def __init__(self):
        self.rules = {
            POSType.S: [[POSType.NP, POSType.VP]],
            POSType.NP: [
                [POSType.Det, POSType.Noun],
                [POSType.Det, POSType.Adj, POSType.Noun],
                [POSType.Noun],
            ],
            POSType.VP: [[POSType.Verb, POSType.NP], [POSType.Verb, POSType.PP]],
            POSType.PP: [[POSType.Prep, POSType.NP]],
            POSType.Det: ["<det>"],
            POSType.Noun: ["<noun>"],
            POSType.Adj: ["<adj>"],
            POSType.Verb: ["<verb>"],
            POSType.Prep: ["<prep>"],
        }

    def get_rules(self, rule_name):
        if rule_name not in self.rules:
            raise RuleNotFoundError(f"Rule '{rule_name}' not found.")
        return self.rules[rule_name]

    def add_rule(self, rule_name, rule_definition):
        if rule_name in self.rules:
            self.rules[rule_name].append(rule_definition)
        else:
            self.rules[rule_name] = [rule_definition]
