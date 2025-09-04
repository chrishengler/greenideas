from greenideas.rules.default_english_rules.parts_of_speech.default_english_pos_types import (
    DefaultEnglishPOSType,
)
from greenideas.rules.expansion_spec import ExpansionSpec
from greenideas.rules.grammar_rule import GrammarRule
from greenideas.rules.source_spec import SourceSpec

# AdvP -> Adv
advp__adv = GrammarRule(
    SourceSpec(DefaultEnglishPOSType.AdvP),
    [ExpansionSpec(DefaultEnglishPOSType.Adv)],
)

# AdvP -> Adv conj Adv
advp__adv_conj_adv = GrammarRule(
    SourceSpec(DefaultEnglishPOSType.AdvP),
    [
        ExpansionSpec(DefaultEnglishPOSType.Adv),
        ExpansionSpec(DefaultEnglishPOSType.SimpleConj),
        ExpansionSpec(DefaultEnglishPOSType.Adv),
    ],
    weight=0.2,
)

# AdvP -> PP
advp__pp = GrammarRule(
    SourceSpec(DefaultEnglishPOSType.AdvP),
    [ExpansionSpec(DefaultEnglishPOSType.PP)],
)

advP_expansions = [
    advp__adv,
    advp__adv_conj_adv,
    advp__pp,
]
