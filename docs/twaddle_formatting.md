# Twaddle Formatting

The Twaddle formatting system converts a syntax tree into a Twaddle input string. This process involves walking through the tree and converting each leaf node into an appropriate Twaddle tag while respecting the structural relationships defined by the intermediate nodes.

## Overview

The formatting process uses three main components:

1. `TwaddleFormatter`: The main orchestrator that walks through the tree
2. `TwaddleFormattingHandler`: Protocol defining how to format specific types of nodes
3. `FormattingContext`: Maintains state during tree traversal (spacing, punctuation, etc.)

## The Formatting Process

When a syntax tree is processed:

1. The formatter walks through the tree depth-first
2. For each node:
   - Applies any pre-punctuation defined on the node
   - If it's a leaf node, converts it to a Twaddle tag using the appropriate formatter
   - Otherwise, processes its children
   - Applies any post-punctuation defined on the node
   - Manages spacing between elements

## Creating Formatting Handlers

Each part of speech that can be a leaf node needs a corresponding formatting handler that implements the `TwaddleFormattingHandler` protocol. A formatting handler is responsible for:

1. Converting a node's grammatical attributes into the appropriate Twaddle tag form
2. Selecting the correct dictionary name
3. Adding any necessary class specifiers

Example implementation:

```python
from greenideas.twaddle.twaddle_tag import build_twaddle_tag
from greenideas.parts_of_speech.pos_node import POSNode

class MyNounFormattingHandler:
    @staticmethod
    def format(node: POSNode) -> str:
        # Validate the node type
        if node.type != MyPOSTypes.NOUN:
            raise TwaddleConversionError(f"Wrong node type: {node.type}")
        
        # Extract relevant attributes
        number = node.attributes.get(MyAttributes.NUMBER)
        case = node.attributes.get(MyAttributes.CASE)
        
        # Determine the form
        form = "sg" if number.is_singular else "pl"
        if case.is_genitive:
            form += "gen"
            
        # Build and return the tag
        return build_twaddle_tag(
            name="noun",
            class_specifier="animate",
            form=form
        )
```

## Setting Up the Formatter

To use the formatting system:

1. Create a `TwaddleFormatter` instance
2. Register formatting handlers for each POS type
3. Call the formatter with your syntax tree

Example:

```python
formatter = TwaddleFormatter()

# Register handlers for each POS type
formatter.register_formatting_handler(MyPOSTypes.NOUN, MyNounFormattingHandler())
formatter.register_formatting_handler(MyPOSTypes.VERB, MyVerbFormattingHandler())
# ... register other handlers

# Format a syntax tree
result = formatter.format(syntax_tree)
```

## Twaddle Tags

A Twaddle tag defines how Twaddle looks up a word from a dictionary. It
is made up of angle brackets `<>` containing a dictionary name and optionally 
specifying the form and class(es) required. The form is separated from the name
by a `.`, and classes are separated by `-`. As such a general form looks 
something like `<name.form-class1-class2>`. The order of form and class is not
strict, and `<name-class1.form-class2>` would be equally valid, though harder
to read. For a fuller description of Twaddle tags, see [the Twaddle 
documentation on Twaddle lookups](https://chrishengler.github.io/twaddle/lookups.html). 

The `build_twaddle_tag` function creates Twaddle tags with the following components:

- Dictionary name: Specifies which dictionary to look up the word in (e.g., "noun", "verb")
- Form: Specifies the grammatical form (e.g., "sg" for singular, "pl" for plural)
- Class specifier: Optional qualifier for the word class (e.g., "animate" for nouns)

Forms and classes must match those defined within the loaded Twaddle 
dictionaries.

Example tag: `<verb.2pl-monovalent>` represents a monovalent noun, conjugated
for the second person plural.

## Formatting Context

The `FormattingContext` class manages:

- Spacing between words
- Accumulated string value
- State information during tree traversal

It should not be necessary to interact with the `FormattingContext` directly.