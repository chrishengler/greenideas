import logging
import random

from greenideas.attributes.grammatical_attribute import GrammaticalAttribute
from greenideas.exceptions import RuleNotFoundError
from greenideas.parts_of_speech.pos_node import POSNode
from greenideas.parts_of_speech.pos_type_base import POSType
from greenideas.rules.expansion_spec import INHERIT, ExpansionSpec
from greenideas.rules.grammar_ruleset import GrammarRuleset

logger = logging.getLogger(__name__)


class GrammarEngine:
    def __init__(self, ruleset: GrammarRuleset):
        self.ruleset = ruleset

    def generate_tree(self, start: POSNode | POSType) -> POSNode:
        logger.info("\n\nNEW TREE")
        if isinstance(start, POSNode):
            node = start
            self._assign_random_attributes(node)
        elif isinstance(start, POSType):
            node = POSNode(type=start)
            self._assign_random_attributes(node)
        else:
            raise ValueError("start must be a POSType or POSNode")
        if len(self.ruleset.get_applicable_rules(node)) == 0:
            raise RuleNotFoundError(f"No rule found to expand type {node.type}")
        logger.info(node.attributes)
        result = self._expand_to_tree(node)
        logger.info(result)
        return result

    def _expand_to_tree(self, node: POSNode) -> POSNode:
        rules = self.ruleset.get_applicable_rules(node)
        if not rules:
            return node
        rule = random.choices(rules, weights=[r.weight for r in rules])[0]
        logger.info(f"expanding {node.type} with rule {rule}\n\n\n")
        children = []
        for _, spec in enumerate(rule.expansion):
            if isinstance(spec, ExpansionSpec):
                child = POSNode(type=spec.pos_type, depth=node.depth + 1)
                child.space_follows = spec.space_follows
                child.pre_punctuation = spec.pre_punctuation
                child.post_punctuation = spec.post_punctuation
                for attr_type, constraint in spec.attribute_constraints.items():
                    if constraint is not None:
                        if constraint == INHERIT:
                            child.attributes.set(
                                attr_type, node.attributes.get(attr_type)
                            )
                        elif isinstance(constraint, list):
                            child.attributes.set(
                                attr_type, GrammaticalAttribute.random_from(constraint)
                            )
                        else:
                            child.attributes.set(attr_type, constraint)
                self._assign_random_attributes(child)
                children.append(self._expand_to_tree(child))
        node.children = children
        return node

    def _assign_random_attributes(self, node: POSNode) -> None:
        for attr_type in self.ruleset.get_relevant_attributes(node.type):
            if attr_type not in node.attributes:
                possible_values = list(attr_type.value_type)
                node.attributes.set(
                    attr_type, GrammaticalAttribute.random_from(possible_values)
                )
