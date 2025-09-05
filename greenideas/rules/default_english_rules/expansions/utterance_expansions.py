from greenideas.rules.default_english_rules.parts_of_speech.default_english_pos_types import (
    DefaultEnglishPOSType,
)
from greenideas.rules.expansion_spec import ExpansionSpec
from greenideas.rules.grammar_rule import GrammarRule
from greenideas.rules.source_spec import SourceSpec

u__s = GrammarRule(
    SourceSpec(DefaultEnglishPOSType.Utterance),
    [ExpansionSpec(DefaultEnglishPOSType.S, post_punctuation=".")],
)

u_expansions = [u__s]
