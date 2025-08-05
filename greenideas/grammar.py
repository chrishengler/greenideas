from greenideas.parts_of_speech.pos_types import POSType
from greenideas.rules.grammar_rule import GrammarRule


class Grammar:
    def __init__(self):
        self.rules = {}

    def add_rule(self, rule: GrammarRule):
        part_of_speech = rule.part_of_speech
        if part_of_speech in self.rules:
            self.rules[part_of_speech].append(rule)
        else:
            self.rules[part_of_speech] = [rule]

    def clear_rules(self):
        self.rules = {}

    def get_rules(self, part_of_speech: POSType) -> list[GrammarRule]:
        return self.rules.get(part_of_speech, [])

    def has_expansion(self, part_of_speech: POSType) -> bool:
        return part_of_speech in self.rules
