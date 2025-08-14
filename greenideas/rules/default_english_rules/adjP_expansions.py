from greenideas.parts_of_speech.pos_types import POSType
from greenideas.rules.expansion_spec import ExpansionSpec
from greenideas.rules.grammar_rule import GrammarRule
from greenideas.rules.source_spec import SourceSpec

# adjP -> Adj
adjP__adj = GrammarRule(
    SourceSpec(POSType.AdjP),
    [
        ExpansionSpec(
            POSType.Adj,
        )
    ],
)

# adjP -> adjP conj adjP
adjP__adjP_conj_adjP = GrammarRule(
    SourceSpec(POSType.AdjP),
    [
        ExpansionSpec(POSType.AdjP),
        ExpansionSpec(POSType.CoordConj),
        ExpansionSpec(POSType.AdjP),
    ],
    weight=0.1,
)

adjP_expansions = [adjP__adj, adjP__adjP_conj_adjP]
