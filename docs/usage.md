# Usage

To use Green Ideas, import the main classes and provide a root node to start generating a tree. Here is a simple example of a runnable file which outputs the sentence
structure and twaddle string, using the included rules for generating English language sentences:

```python
from greenideas.grammar_engine import GrammarEngine
from greenideas.parts_of_speech.pos_types import POSType
from greenideas.rules.default_english_rules.default_rules import default_rules
from greenideas.twaddle.default_formatters.default_formatting_handlers import default_formatting_handlers
from greenideas.twaddle.twaddle_formatter import TwaddleFormatter

def main():
    engine = GrammarEngine()
    engine.add_ruleset(default_rules)
    tree = engine.generate_tree(POSType.S)
    print(tree)

    formatter = TwaddleFormatter()
    for type, handler in default_formatting_handlers.items():
        formatter.register_formatting_handler(type, handler)

    twaddle_string = formatter.format_as_sentence(tree)
    print(twaddle_string)

if __name__ == "__main__":
    main()
```

See [greenideas-dict](https://github.com/chrishengler/greenideas-dict) for official twaddle dictionaries which allow twaddle to turn this output into actual English language sentences.
