from typing import List

from greenideas.attributes.attribute_set import AttributeSet
from greenideas.attributes.attribute_type import AttributeType
from greenideas.attributes.propagation_rule import PropagationRule
from greenideas.pos_node import POSNode
from greenideas.pos_types import POSType


class AttributePropagator:
    def __init__(self) -> None:
        self.rules: List[PropagationRule] = []
        self._setup_default_rules()

    def _setup_default_rules(self) -> None:
        """Initialize the default propagation rules."""
        # S to NP and VP
        self.rules.append(
            PropagationRule(
                source_type=POSType.S,
                target_type=POSType.NP,
                attributes={AttributeType.PERSON, AttributeType.NUMBER},
            )
        )
        self.rules.append(
            PropagationRule(
                source_type=POSType.S,
                target_type=POSType.VP,
                attributes={
                    AttributeType.PERSON,
                    AttributeType.NUMBER,
                    AttributeType.TENSE,
                },
            )
        )

        # VP to its children
        self.rules.append(
            PropagationRule(
                source_type=POSType.VP,
                target_type=POSType.Verb,
                attributes={
                    AttributeType.PERSON,
                    AttributeType.NUMBER,
                    AttributeType.TENSE,
                },
            )
        )
        self.rules.append(
            PropagationRule(
                source_type=POSType.VP, target_type=POSType.NP, attributes={}
            )
        )

        # NP to its children
        self.rules.append(
            PropagationRule(
                source_type=POSType.NP,
                target_type=POSType.Det,
                attributes={AttributeType.PERSON, AttributeType.NUMBER},
            )
        )
        self.rules.append(
            PropagationRule(
                source_type=POSType.NP,
                target_type=POSType.Noun,
                attributes={AttributeType.PERSON, AttributeType.NUMBER},
            )
        )

    def propagate(self, node: POSNode) -> None:
        """
        Propagate attributes from node to its children according to propagation rules.
        All attributes are propagated, optimization of which are relevant will happen later.

        Args:
            node: The node to propagate attributes from
        """
        # Find all rules that apply to this node type as source
        applicable_rules = [
            rule for rule in self.rules if rule.source_type == node.type
        ]

        for child in node.children:
            # Find rules that apply to this specific child
            child_rules = [
                rule for rule in applicable_rules if rule.target_type == child.type
            ]

            for rule in child_rules:
                # Create a new attribute set for propagated values
                child_attrs = AttributeSet()

                # Propagate ALL attributes that exist in the parent
                for attr_type in rule.attributes:
                    value = node.attributes.get(attr_type)
                    if value is not None:
                        child_attrs.set(attr_type, value)

                # Merge with existing attributes, prioritizing propagated values
                child.attributes = child_attrs.merge(child.attributes)
