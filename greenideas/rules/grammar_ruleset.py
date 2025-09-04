from typing import Callable

from greenideas.attributes.grammatical_attribute import GrammaticalAttribute
from greenideas.exceptions import InvalidGrammarRule
from greenideas.parts_of_speech.pos_type_base import POSType
from greenideas.rules.expansion_spec import ExpansionSpec
from greenideas.rules.grammar_rule import GrammarRule
from greenideas.rules.source_spec import SourceSpec


class GrammarRuleset:
    def __init__(
        self, pos_attribute_relevance: Callable[[POSType], list[GrammaticalAttribute]]
    ):
        self.rules = list()
        self.pos_attribute_relevance = pos_attribute_relevance

    def add(self, rule: GrammarRule):
        self._validate_rule_source(rule.source)
        self.rules.append(rule)

    def _validate_rule_source(self, source: SourceSpec):
        for attr, val in source.attribute_constraints.items():
            if attr not in self.pos_attribute_relevance(source.pos_type):
                raise InvalidGrammarRule(
                    f"SourceSpec includes constraints on {str(attr)}, not defined as relevant for {source.pos_type}"
                )
            if not isinstance(val, attr.value_type):
                if isinstance(val, list) and all(
                    isinstance(v, attr.value_type) for v in val
                ):
                    continue
                raise TypeError(
                    f"Value for {attr.name} must be of type {str(attr)} (or list of), got {type(val)}"
                )

    def _validate_rule_expansion(self, expansion: ExpansionSpec):
        for attr in expansion.attribute_constraints:
            if attr not in self.pos_attribute_relevance(expansion.pos_type):
                raise InvalidGrammarRule(
                    f"Attribute constraints on {attr}, not defined as relevant for {expansion.pos_type}"
                )

    def add_rules(self, rules: list[GrammarRule]):
        for rule in rules:
            self.add(rule)
