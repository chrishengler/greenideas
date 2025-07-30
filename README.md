# Green Ideas

Green Ideas is a Python package designed to generate grammatically valid but semantically nonsensical English sentences using a generative grammar approach. The package employs recursive rewrite rules to create sentence structures and converts these structures into templates compatible with the `twaddle` package for language templating.

## Features

The project is in early development and currently does very little indeed. Once completed, core features
will include:

- Generation of trees describing valid English sentence structures
- Support for recursive rewrite rules for sentence structure generation.
- Converting sentence trees into twaddle-compatible templates.
- Modular design allowing for easy extension and modification of grammar rules.

## Installation

For now, just download the repository from Github and handle the package by hand. The package will
be added to PyPi at a later date to allow installation via pip, etc.

The package uses Poetry for dependency management, dependencies can be installed by running

```bash
poetry install
```

## Usage

To use the `greenideas` package, you can (or at least you will be able to, at some point) import the main classes from the package and start generating sentences. Here’s a simple example:

```python
from greenideas.grammar_engine import GrammarEngine
from greenideas.tree_to_twaddle import TreeToTwaddle

# Initialize the grammar engine
grammar_engine = GrammarEngine()

# Generate a derivation tree
tree = grammar_engine.generate_tree()

# Convert the tree to a twaddle template
converter = TreeToTwaddle()
template = converter.convert_tree(tree)

print(template)
```

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.