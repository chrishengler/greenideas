import copy
import random

from greenideas.exceptions import RuleNotFoundError
from greenideas.grammar import Grammar
from greenideas.pos_node import POSNode
from greenideas.pos_types import POSType


class GrammarEngine:
    def __init__(self):
        self.grammar = Grammar()

    def add_rule(self, rule_name, rule_definition, weight=1.0):
        self.grammar.add_rule(rule_name, rule_definition, weight)

    def generate_tree(self, start_symbol):
        if not self.grammar.has_rule(start_symbol):
            raise RuleNotFoundError(f"Rule '{start_symbol}' not found.")
        return self._expand_to_tree(start_symbol)

    def _expand_to_tree(self, symbol):
        # Always return a POSNode
        rules = self.grammar.get_rules(symbol)
        if not rules:
            # Terminal: treat as string or POSType
            return POSNode(type_=symbol, children=[], value=None)
        # For now, always use the first rule
        rule = rules[0]
        children = []
        for elem in rule.rhs:
            if self.grammar.has_rule(elem):
                children.append(self._expand_to_tree(elem))
            else:
                # Terminal: could be POSType or str
                if isinstance(elem, POSType):
                    children.append(POSNode(type_=elem, children=[], value=None))
                else:
                    # Terminal string (e.g., 'the')
                    children.append(POSNode(type_=symbol, children=[], value=elem))
        return POSNode(type_=symbol, children=children)

    def annotate_top_down(self, node: POSNode, context: dict):
        """
        Recursively annotate the tree with grammatical features.
        - node: the current POSNode
        - context: dict of inherited features (e.g., {'number': 'singular', 'person': 3, 'tense': 'past'})
        """
        # Merge context into node.attributes, but don't overwrite existing
        for k, v in context.items():
            if k not in node.attributes:
                node.attributes[k] = v

        # Decide new features at this node if needed
        if node.type == POSType.S:
            if "person" not in node.attributes:
                node.attributes["person"] = random.choice([1, 2, 3])
            if "number" not in node.attributes:
                node.attributes["number"] = random.choice(["singular", "plural"])
            if "tense" not in node.attributes:
                node.attributes["tense"] = random.choice(["present", "past"])

        # Pass down relevant features
        for child in node.children:
            child_context = copy.deepcopy(node.attributes)
            if node.type == POSType.S:
                if child.type == POSType.NP:
                    keys = ["person", "number"]
                    child_context = {
                        k: node.attributes[k] for k in keys if k in node.attributes
                    }
                elif child.type == POSType.VP:
                    keys = ["person", "number", "tense"]
                    child_context = {
                        k: node.attributes[k] for k in keys if k in node.attributes
                    }
            elif node.type == POSType.VP:
                if child.type == POSType.Verb:
                    keys = ["person", "number", "tense"]
                    child_context = {
                        k: node.attributes[k] for k in keys if k in node.attributes
                    }
            elif node.type == POSType.NP:
                if child.type == POSType.NP and not child.attributes:
                    child_context = {}
                    child_context["number"] = random.choice(["singular", "plural"])
                    child_context["person"] = random.choice([1, 2, 3])
            self.annotate_top_down(child, child_context)
