# Grammar Concepts

Green Ideas is built around the concept of generative grammar, using recursive rules to expand sentence structures. The main abstractions are:

- **POSNode**: Represents a node in the sentence tree, corresponding to a part of speech (POS) such as Noun, Verb, or Sentence. Each node stores its type, children, and grammatical attributes.
- **GrammarRule**: Defines how a part of speech can be expanded into other parts of speech or terminal symbols. Rules can specify attribute propagation and constraints.
- **ExpansionSpec**: Used within GrammarRule to specify how each child node should inherit or set grammatical attributes. Allows fine-grained control over agreement and feature assignment.
- **SourceSpec**: Used to specify the node types which can be expanded by a rule, and any GrammaticalAttribute-based restrictions on the rules applicability
- **AttributeType / GrammaticalAttribute**: GrammaticalAttribute is a base Enum class used to define the grammatical features (such as aspect, case, number, tense) which can be assigned to nodes. AttributeType provides a convenient list of all defined GrammaticalAttributes. These are used for agreement and feature propagation.

## Example

A simple rule might look like:

```python
GrammarRule(SourceSpec(POSType.S), [
    ExpansionSpec(POSType.NP, {AttributeType.NUMBER: INHERIT, AttributeType.PERSON: INHERIT}),
    ExpansionSpec(POSType.VP, {AttributeType.NUMBER: INHERIT, AttributeType.PERSON: INHERIT})
])
```

This expands a sentence (S) into a noun phrase (NP) and a verb phrase (VP), propagating number and person attributes from the parent to the children.
