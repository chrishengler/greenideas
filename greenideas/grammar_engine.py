import random

from greenideas.attributes.attribute_type import AttributeType
from greenideas.exceptions import RuleNotFoundError
from greenideas.expansion_spec import INHERIT, ExpansionSpec
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

    def generate_tree(self, start: POSNode | POSType) -> POSNode:
        """
        Accepts a POSType or a POSNode. If a POSNode, respects any attributes already set.
        If a POSType, creates a POSNode with all attributes set at random.
        """
        if isinstance(start, POSNode):
            node = start
            # Set any missing attributes at random
            self._assign_random_attributes(node)
        elif isinstance(start, POSType):
            node = POSNode(type=start)
            self._assign_random_attributes(node)
        else:
            raise ValueError("start must be a POSType or POSNode")
        if len(self.grammar.get_rules(node.type)) == 0:
            raise RuleNotFoundError(f"No rule found to expand type {node.type}")
        return self._expand_to_tree(node)

    def _expand_to_tree(self, node: POSNode) -> POSNode:
        # Always return a POSNode
        rules = self.grammar.get_rules(node.type)
        if not rules:
            return node
        rule = rules[0]
        children = []
        for _, spec in enumerate(rule.expansion):
            if isinstance(spec, ExpansionSpec):
                # Create child node
                child = POSNode(type=spec.pos_type)
                # Propagate/inherit/set attributes according to spec
                for attr_type, constraint in spec.attribute_constraints.items():
                    if constraint is not None:
                        print(f"{constraint=}")
                        if constraint == INHERIT:
                            child.attributes.set(
                                attr_type, node.attributes.get(attr_type)
                            )
                        else:
                            # Set required value
                            child.attributes.set(attr_type, constraint)
                # Set any missing attributes at random
                self._assign_random_attributes(child)
                # Recursively expand
                children.append(self._expand_to_tree(child))
        node.children = children
        return node

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
