from greenideas.rules.default_english_rules.parts_of_speech.default_english_pos_types import (
    DefaultEnglishPOSType,
)
from greenideas.rules.expansion_spec import ExpansionSpec
from greenideas.rules.grammar_rule import GrammarRule
from greenideas.rules.source_spec import SourceSpec

# VP_Bare -> Adv VP(bare)
vpBare__adv_vpBare = GrammarRule(
    SourceSpec(DefaultEnglishPOSType.VP_Bare),
    [
        ExpansionSpec(DefaultEnglishPOSType.Adv),
        ExpansionSpec(
            DefaultEnglishPOSType.VP_Bare,
        ),
    ],
    weight=0.2,
)

# VP_Bare -> Verb(bare)
vpBare__vBare = GrammarRule(
    SourceSpec(DefaultEnglishPOSType.VP_Bare),
    [
        ExpansionSpec(
            DefaultEnglishPOSType.Verb_Bare,
        )
    ],
)

vpBare_expansions = [vpBare__adv_vpBare, vpBare__vBare]
