# API Reference

## Defining a Language Grammar

In GreenIdeas, a language is defined as a set of rules which operate
on parts of speech, with reference to various grammatical attributes.
To define a language, it is first necessary to define the parts of 
speech and the grammatical attributes which the language will use.

### Parts of Speech (POS Types)

To define the parts of speech for a language, create a new enum class that inherits from `POSType`:

```python
from greenideas.parts_of_speech.pos_type_base import POSType

class MyLanguagePOSTypes(POSType):
    SENTENCE = "Sentence"
    NOUN = "Noun"
    VERB = "Verb"
    ADJECTIVE = "Adjective"
    DETERMINER = "Determiner
```

### Grammatical Attributes

Define the grammatical attributes for your language by creating a set of 
enums which inherit from `GrammaticalAttribute`:

```python
from enum import auto
from greenideas.attributes.grammatical_attribute import GrammaticalAttribute

class Number(GrammaticalAttribute):
    SINGULAR = auto() 
    PLURAL = auto()

class Tense(GrammaticalAttribute):
    PRESENT = ("pres", 1)
    PAST = ("past", 1)

```

Attributes may be defined simply as `auto()`, in which case all values are
equally likely, or may be defined as a `label, weight` pair. In the latter case,
the `weight` influences the probability of each value when the attribute is 
assigned randomly.

Additionally, define an enum derived from `AttributeType` which lists all 
of the language's attributes, as a (`label`, `GrammaticalAttribute`) pair:

```python
from greenideas.attributes.attribute_type import AttributeType
from mylanguage.attributes import Number, Tense

class MyLanguageAttributes(AttributeType):
    NUMBER = ("number", NUMBER)
    TENSE = ("tense", TENSE)

```


### Grammar Rules

#### The GrammarRuleset Class

The `GrammarRuleset` class serves as the container for all grammar rules in your language. Initialize it with a function that defines which attributes are relevant for each part of speech:

```python
def get_relevant_attributes(pos_type: POSType) -> list[GrammaticalAttribute]:
    if pos_type == MyLanguagePOSTypes.SENTENCE:
        return [MyLanguageAttributes.NUMBER, MyLanguageAttributes.TENSE]
    if pos_type == MyLanguagePOSTypes.DETERMINER:
        return [MyLanguageAttributes.NUMBER]
    if pos_type == MyLanguagePOSTypes.NOUN:
        return [MyLanguageAttributes.NUMBER]
    elif pos_type == MyLanguagePOSTypes.VERB:
        return [MyLanguageAttributes.NUMBER, MyLanguageAttributes.TENSE]
    return []

ruleset = GrammarRuleset(pos_attribute_relevance=get_relevant_attributes)
```

In the simple example above it is practical for this function to be based
on `if .. elif` statements. For more realistic complexity this may be
inadvisable. The default English ruleset included in the GreenIdeas package
defines a dictionary, and raises an error when queried for a `POSType` not
defined. This pattern ensures that the set of relevant attributes is
defined for all `POSTypes`, as an error will be raised on loading
a rule for any type without an attribute set explicitly defined.

#### Creating Grammar Rules

Each `GrammarRule` defines how a node in the syntax tree can be expanded. A rule consists of:
1. A `SourceSpec` defining what kind of node the rule applies to
2. A list of `ExpansionSpec` objects defining the child nodes

Example:

```python
from greenideas.rules.expansion_spec import ExpansionSpec, INHERIT
from greenideas.rules.source_spec import SourceSpec

from mylanguage.pos_types import MyLanguagePOSTypes

generic_sentence_source = SourceSpec(
    pos_type=MyLanguagePOSType.SENTENCE
)

generic_expansion = [
    ExpansionSpec(
        pos_type=MyLanguagePOSTypes.DETERMINER,
        attribute_constraints={MyLanguageAttributes.NUMBER: INHERIT}
    )
    ExpansionSpec(
        pos_type=MyLanguagePOSTypes.NOUN,
        attribute_constraints={MyLanguageAttributes.NUMBER: INHERIT}
    ),
    ExpansionSpec(
        pos_type=MyLanguagePOSTypes.VERB,
        attribute_constraints={MyLanguageAttributes.NUMBER: INHERIT,
                               MyLanguageAttributes.TENSE: Tense.PRESENT}
    )
]

plural_sentence_source = SourceSpec(
    pos_type=MyLanguagePOSTypes.SENTENCE,
    attribute_constraints={MyLanguageAttributes.NUMBER: Number.PLURAL}
)

plural_expansion = [
    ExpansionSpec(
        pos_type=MyLanguagePOSTypes.NOUN,
        attribute_constraints={MyLanguageAttributes.NUMBER: INHERIT}
    ),
    ExpansionSpec(
        pos_type=MyLanguagePOSTypes.VERB,
        attribute_constraints={MyLanguageAttributes.NUMBER: INHERIT,
                               MyLanguageAttributes.TENSE: INHERIT}

    )
]



generic_rule = GrammarRule(source=generic_sentence_source, expansion=generic_expansion, weight=1)
plural_only_rule = GrammarRule(source=plural_sentence_source, expansion=plural_expansion, weight=0.5)

ruleset.add_rule(generic_rule)
ruleset.add_rule(plural_only_rule)
```

In the examples above, the rule `generic_rule` defines that any sentence node
can be expanded into a sequence of nodes with the types `DETERMINER`, `NOUN`, 
`VERB` in that order. The `NUMBER` attribute of the sentence is propagated
through to each node, and the `TENSE` of the verb is (for the sake of
demonstration) restricted to be present-tense only, regardless of the `TENSE`
attribute of the original `SENTENCE` node. This expansion would thus produce 
sentences of the form `A hat falls`, `The kittens run`.

The rule `plural_only_rule` defines that sentences may be expanded into a sequence of nodes with the types
`NOUN`, `VERB` in that order. The `NUMBER` attribute is propagated through
to both terminal nodes, and the `TENSE` attribute is propagated to the verb
node. As such, this rule may produce sentences such as `People eat`, 
`Balloons fly`. The `attribute_constraints` on the `SouceSpec` ensure that 
this rule is not applied when the `SENTENCE` node has `NUMBER` attribute 
`Number.PLURAL`, avoiding the production of sentences like `Umbrella opens`, 
with a singular noun and no determiner.

The `weight` parameter of a `GrammarRule` influences the chance that the rule
will be selected when expanding a node to which the rule is applicable, and 
has a default value of `1` if not specified.

#### SourceSpec

The `SourceSpec` class defines which nodes a rule can be applied to:
- `pos_type`: The part of speech this rule expands
- `attribute_constraints`: A dictionary mapping attributes to
  - Single value: The node must have exactly this value
  - List of values: The node must have one of these values
  Constraints may only be placed on attributes defined as [relevant](api_reference.md#the-grammarruleset-class) for the source POS type.
  The rule will be considered applicable only if all constraints are satisfied.
  Attributes with no constraints applied can be omitted from the dictionary.

#### ExpansionSpec

The `ExpansionSpec` class defines how to create child nodes:
- `pos_type`: The part of speech for the child node
- `attribute_constraints`: A dictionary mapping relevant attributes to:
  - INHERIT: The child will inherit the value from the parent
  - A specific value: The child will have this value
  - A list of values: The attribute will be randomly chosen from these values
  Constraints may only be placed on attributes defined as [relevant](api_reference.md#the-grammarruleset-class) for the expansion POS type.
  Relevant attributes with no constraints will be assigned values randomly

## Core Classes

### POSNode
Represents a node in the syntax tree:
- `type`: The part of speech (POSType)
- `children`: List of child POSNodes
- `attributes`: Set of grammatical attributes

### AttributeSet
A collection of grammatical attributes for a node. Attributes are validated 
against the defined `pos_attribute_relevance` function to ensure only relevant 
attributes are assigned to each part of speech. 

## Generating Trees

Once you have defined your `POSType`s and `GrammaticalAttribute`s, created your
`GrammarRuleset`, and added your `GrammarRule`s to it, you are ready to generate
sentence trees. 

To do this, initialise a `GrammarEngine` with your `GrammarRuleset` and pass
the root node for your tree into its `generate_tree` method.

```python
from greenideas.grammar_engine import GrammarEngine
from mylanguage.grammar_ruleset import my_grammar_ruleset
from mylanguage.pos_types import MyLanguagePOSTypes

engine = GrammarEngine(my_grammar_ruleset)
tree = engine.generate_tree(MyLanguagePOSTypes.SENTENCE)
```

The `GrammarEngine` will create a `POSNode` of the specified type, and assign
it random values to all relevant `GrammaticalAttribute`s (if you wish to
specify particular starting attributes, you can also pass a `POSNode` into
`generate_tree`). It will then recursively expand each node according to the 
rules defined in the `GrammarRuleset` until no further expansion is possible. 
Each node's expansion is chosen randomly from the set of all applicable rules 
in the `GrammarRuleset`.
