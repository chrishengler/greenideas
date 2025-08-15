# API Reference

## POSNode
Represents a node in the sentence tree.
- `type`: The part of speech (POSType)
- `children`: List of child POSNodes
- `attributes`: Grammatical attributes (AttributeSet)

## GrammarRule
Defines how a POSNode can be expanded.
- `part_of_speech`: The parent POS type
- `expansion`: List of ExpansionSpec objects
- `weight`: Rule weight (for probabilistic grammars)
- Methods: `get_child_spec(idx)`

## ExpansionSpec
Specifies how a child node is constructed in a rule.
- `pos_type`: The POS type for the child
- `attribute_constraints`: Dict of AttributeType to value, INHERIT, or None
- Methods: `get_constraint(attr_type)`

## SourceSpec
Specifies which kind of node may be expanded by a rule.
- `pos_type`: The POS type for the source node
- `attribute_constraints`: Dict of AttributeType to values required/accepted for the rule to be applicable

## AttributeType / GrammaticalAttribute
Enumerates grammatical features.
- Examples: `NUMBER`, `PERSON`, `TENSE`, `CASE`

More thorough documentation will be provided at a later stage of development.
Until then, refer to the source code or the default English rules for further guidance.
