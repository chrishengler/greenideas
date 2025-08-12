from greenideas.parts_of_speech.pos_types import POSType
from greenideas.rules.expansion_spec import ExpansionSpec
from greenideas.rules.grammar_rule import GrammarRule
from greenideas.rules.source_spec import SourceSpec

# VP_Bare -> Adv VP(bare)
vpBare__adv_vpBare = GrammarRule(
    SourceSpec(POSType.VP_Bare),
    [
        ExpansionSpec(POSType.Adv),
        ExpansionSpec(
            POSType.VP_Bare,
        ),
    ],
    weight=0.2,
)

# VP_Bare -> Verb(bare)
vpBare__vBare = GrammarRule(
    SourceSpec(POSType.VP_Bare),
    [
        ExpansionSpec(
            POSType.Verb_Bare,
        )
    ],
)

vpBare_expansions = [vpBare__adv_vpBare, vpBare__vBare]
