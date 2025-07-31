You are helping me build a Python package called `green-ideas`. The purpose of this package is to generate grammatically valid but semantically nonsensical English sentences, using a simplified generative grammar approach. The package will:

- Use recursive rewrite rules to generate sentence structures (e.g., S → NP VP).
- Convert generated structures into templated strings that are valid inputs for a separate package called `twaddle`.
- `twaddle` is a mad-libs-style generator which replaces tags like `<noun>`, `<verb.s>`, `<adj>` etc. with appropriate random words. It supports grammatical tags (e.g., verb forms), specified using a dot syntax like `<verb.s>` (3rd person singular present) or `<verb.ed>` (past tense).
- `twaddle` allows labelling of tags to ensure recall or avoidance of the word chosen for that tag (e.g. "the <adj::=a> <noun::=thing> <verb.ed> the <adj::!=a> <noun::=thing>" applies the tag `a` to the first adjective, then requires the second adjective to be different (`!=a`), while requiring both nouns to be identical by applying the same tag to each).

Important constraints:
- This package will not perform semantic validation or parse real-world text—it only generates structures.
- It will only target English grammar, assuming a simplified subset (e.g., it does not need to produce idiomatic phrases or sentences with highly irregular embeddings).
- A central feature is the mapping from parse trees to fully specified twaddle templates, including resolving features like subject-verb agreement and determiner-noun agreement.
- It must support expanding multiple grammars (e.g., different S rules, NP rules, etc.).
- The system must be modular, so grammars can be extended or modified easily.
- The output must be a valid twaddle string (e.g., "<det> <adj> <noun> <verb.ed> <prep> <det> <adj> <noun>").
- The package is not concerned with vocabulary. It operates purely on the grammatical level, producing a 
sentence tree with annotations to indicate relevant properties like number, tense, animacy, such that the 
appropriate twaddle output can be produced.

What you should generate:
- A well-structured Python package scaffold (using the `greenideas` folder for implementation and the `tests` folder for tests).
- A core grammar engine that uses rewrite rules to produce derivation trees with appropriate annotations to allow for agreement between elements.
- A converter that turns those trees into twaddle-compatible templates.
- A basic grammar with rules for NP, VP, PP, etc.
- Meaningful unit tests (in `tests/`) that test:
    - Trees are correctly expanded from rules.
    - Agreement is correctly resolved (e.g., third person singular subjects produce `<verb.s>`).
    - Twaddle templates are well-formed.
    - Common failure modes, like missing rule branches, are caught.

The package is to be developed targeting Python 3.11+, using poetry for dependency management. Use idiomatic Python, but avoid premature overengineering. Use dataclasses if helpful. Tests should be insightful and sensitive to actual logic failures, not just language features.