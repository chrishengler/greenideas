from greenideas.parts_of_speech.pos_types import POSType
from greenideas.rules.expansion_spec import ExpansionSpec
from greenideas.rules.grammar_rule import GrammarRule
from greenideas.rules.source_spec import SourceSpec

# AdvP -> Adv
advp__adv = GrammarRule(
    SourceSpec(POSType.AdvP),
    [ExpansionSpec(POSType.Adv)],
)

# AdvP -> PP
advp__pp = GrammarRule(
    SourceSpec(POSType.AdvP),
    [ExpansionSpec(POSType.PP)],
)

advP_expansions = [
    advp__adv,
    advp__pp,
]
