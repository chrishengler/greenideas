[![Python application](https://github.com/chrishengler/greenideas/actions/workflows/python-app.yml/badge.svg)](https://github.com/chrishengler/greenideas/actions/workflows/python-app.yml)

# Green Ideas

Green Ideas is a Python package designed to generate grammatically valid but semantically nonsensical sentences. It is effectively a generative grammar engine, employing recursive rewrite rules to create sentence structures. It can then convert these structures into templates compatible with the `twaddle` package for language templating.

## Features

Greenideas defines a grammar engine which expands a root sentence node into a full sentence
tree, according to a variety of user-defined rules. Documentation for defining these rules will come at a later date. The package includes a pre-written set of rules which produce (mostly) grammatically valid English sentences. 

The key features of the package are:

- Generation of trees describing valid English sentence structures
- Support for recursive rewrite rules for sentence structure generation.
- Converting sentence trees into twaddle-compatible templates.
- Modular design allowing for easy extension and modification of grammar rules.

## Installation

The package can be downloaded manually from Github or installed via pip:

```bash
pip install greenideas
```

The package uses Poetry for dependency management, dependencies can be installed by running

```bash
poetry install
```

## Usage

To use the `greenideas` package, you can (or at least you will be able to, at some point) import the main classes from the package, provide the location of your twaddle dictionaries, and start generating sentences. The __main__.py file offers a simple example:

```python
import readline  # noqa: F401
import sys

from twaddle.runner import TwaddleRunner

from greenideas.grammar_engine import GrammarEngine
from greenideas.parts_of_speech.pos_types import POSType
from greenideas.rules.default_english_rules.default_rules import default_rules
from greenideas.twaddle.default_formatters.default_formatting_handlers import (
    default_formatting_handlers,
)
from greenideas.twaddle.twaddle_formatter import TwaddleFormatter


def main():
    if len(sys.argv) < 2:
        print("argument required: path to directory containing dictionary files")
        return
    dictionary_path = sys.argv[1]
    twaddle_runner = TwaddleRunner(dictionary_path)

    engine = GrammarEngine()
    engine.add_ruleset(default_rules)
    tree = engine.generate_tree(POSType.S)
    print(tree)

    formatter = TwaddleFormatter()
    for type, handler in default_formatting_handlers.items():
        formatter.register_formatting_handler(type, handler)

    twaddle_string = formatter.format_as_sentence(tree)
    print(twaddle_string)
    print(twaddle_runner.run_sentence(twaddle_string))
```

An official set of twaddle dictionaries for use with the default English language rules is
available at https://github.com/chrishengler/greenideas-dict

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.