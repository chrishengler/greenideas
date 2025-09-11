from greenideas.rules.default_english_rules.attributes.default_english_attribute_type import (
    DefaultEnglishAttributeType,
)
from greenideas.rules.default_english_rules.attributes.mood import Mood
from greenideas.rules.default_english_rules.parts_of_speech.default_english_pos_types import (
    DefaultEnglishPOSType,
)
from greenideas.rules.expansion_spec import ExpansionSpec
from greenideas.rules.grammar_rule import GrammarRule
from greenideas.rules.source_spec import SourceSpec

u__s = GrammarRule(
    SourceSpec(
        DefaultEnglishPOSType.Utterance,
        {DefaultEnglishAttributeType.MOOD: Mood.DECLARATIVE},
    ),
    [ExpansionSpec(DefaultEnglishPOSType.S, post_punctuation=".")],
)

u__q = GrammarRule(
    SourceSpec(
        DefaultEnglishPOSType.Utterance,
        {
            DefaultEnglishAttributeType.MOOD: Mood.INTERROGATIVE,
        },
    ),
    [ExpansionSpec(DefaultEnglishPOSType.Q, post_punctuation="?")],
)

u__s_conj_q = GrammarRule(
    SourceSpec(
        DefaultEnglishPOSType.Utterance,
        {
            DefaultEnglishAttributeType.MOOD: Mood.INTERROGATIVE,
        },
    ),
    [
        ExpansionSpec(DefaultEnglishPOSType.S, post_punctuation=","),
        ExpansionSpec(DefaultEnglishPOSType.SimpleConj),
        ExpansionSpec(DefaultEnglishPOSType.Q, post_punctuation="?"),
    ],
    weight=0.2,
)

u_expansions = [u__s, u__q, u__s_conj_q]
