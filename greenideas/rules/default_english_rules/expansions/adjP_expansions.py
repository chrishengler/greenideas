from greenideas.rules.default_english_rules.parts_of_speech.default_english_pos_types import (
    DefaultEnglishPOSType,
)
from greenideas.rules.expansion_spec import ExpansionSpec
from greenideas.rules.grammar_rule import GrammarRule
from greenideas.rules.source_spec import SourceSpec

# adjP -> Adj
adjP__adj = GrammarRule(
    SourceSpec(DefaultEnglishPOSType.AdjP),
    [
        ExpansionSpec(
            DefaultEnglishPOSType.Adj,
        )
    ],
)

# adjP -> adjP conj adjP
adjP__adjP_conj_adjP = GrammarRule(
    SourceSpec(DefaultEnglishPOSType.AdjP),
    [
        ExpansionSpec(DefaultEnglishPOSType.AdjP),
        ExpansionSpec(DefaultEnglishPOSType.SimpleConj),
        ExpansionSpec(DefaultEnglishPOSType.AdjP),
    ],
    weight=0.1,
)

# adjP -> djP deg adjP
adjP__deg_adj = GrammarRule(
    SourceSpec(DefaultEnglishPOSType.AdjP),
    [
        ExpansionSpec(DefaultEnglishPOSType.Deg),
        ExpansionSpec(DefaultEnglishPOSType.Adj),
    ],
    # weight = 0.1,
)

adjP_expansions = [adjP__adj, adjP__adjP_conj_adjP, adjP__deg_adj]
