from greenideas.parts_of_speech.pos_node import POSNode
from greenideas.parts_of_speech.pos_types import POSType
from greenideas.rules.grammar_rule import GrammarRule


class Grammar:
    def __init__(self):
        self.rules = {}

    def add_rule(self, rule: GrammarRule):
        part_of_speech = rule.pos
        if part_of_speech in self.rules:
            self.rules[part_of_speech].append(rule)
        else:
            self.rules[part_of_speech] = [rule]

    def clear_rules(self):
        self.rules = {}

    def get_rules(self, part_of_speech: POSType) -> list[GrammarRule]:
        return self.rules.get(part_of_speech, [])

    def get_applicable_rules(self, node: POSNode) -> list[GrammarRule]:
        candidates = self.get_rules(node.type)
        rules = [
            candidate
            for candidate in candidates
            if candidate.is_applicable_to_node(node)
        ]
        return rules

    def has_expansion(self, part_of_speech: POSType) -> bool:
        return part_of_speech in self.rules
