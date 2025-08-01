import random

from greenideas.attributes.attribute_set import AttributeSet
from greenideas.attributes.attribute_type import AttributeType
from greenideas.attributes.propagation import AttributePropagator
from greenideas.exceptions import RuleNotFoundError
from greenideas.grammar import Grammar
from greenideas.grammar_rule import GrammarRule
from greenideas.pos_node import POSNode
from greenideas.pos_types import POSType


class GrammarEngine:
    def __init__(self):
        self.grammar = Grammar()

    def add_rule(self, rule: GrammarRule):
        self.grammar.add_rule(rule)

    def clear_rules(self):
        self.grammar.clear_rules()

    def generate_tree(self, start_symbol: POSType) -> POSNode:
        if not self.grammar.has_expansion(start_symbol):
            raise RuleNotFoundError(f"Rule '{start_symbol}' not found.")
        return self._expand_to_tree(start_symbol)

    def _expand_to_tree(self, part_of_speech) -> POSNode:
        # Always return a POSNode
        rules = self.grammar.get_rules(part_of_speech)
        if not rules:
            return POSNode(type=part_of_speech, children=[], value=None)
        # For now, always use the first rule
        rule = rules[0]
        children = []
        for elem in rule.expansion:
            if self.grammar.has_expansion(elem):
                children.append(self._expand_to_tree(elem))
            else:
                # Terminal: could be POSType or str
                if isinstance(elem, POSType):
                    children.append(POSNode(type=elem, children=[], value=None))
                else:
                    # Terminal string (e.g., 'the')
                    children.append(
                        POSNode(type=part_of_speech, children=[], value=elem)
                    )

        return POSNode(type=part_of_speech, children=children)

    def _assign_random_attributes(self, node: POSNode) -> None:
        """
        Assign random values to any attributes that haven't been set by propagation.
        ALL attributes are assigned to ALL nodes, optimization will happen later.

        Args:
            node: The node to assign attributes to
        """
        # Get all possible attributes from AttributeType enum
        all_attributes = list(AttributeType)

        # For any attribute not already set, assign a random value
        for attr_type in all_attributes:
            if attr_type not in node.attributes:
                possible_values = list(attr_type.value_type)
                node.attributes.set(attr_type, random.choice(possible_values))

    def annotate_top_down(self, node: POSNode) -> None:
        """
        Recursively annotate the tree with grammatical features.
        First propagates existing attributes according to rules,
        then randomly assigns any missing attributes.
        ALL nodes receive ALL attributes - optimization will happen later.

        Args:
            node: The root node of the tree to annotate
        """
        # Step 1: Start with the sentence node
        if node.type == POSType.S:
            attrs = AttributeSet()
            # Set ALL attributes on the root node
            for attr_type in AttributeType:
                possible_values = list(attr_type.value_type)
                attrs.set(attr_type, random.choice(possible_values))
            node.attributes = attrs

        # Step 2: Propagate attributes according to rules
        propagator = AttributePropagator()
        propagator.propagate(node)

        # Step 3: Assign random values to any unset attributes
        self._assign_random_attributes(node)

        # Step 4: Recursively process all children
        for child in node.children:
            self.annotate_top_down(child)
