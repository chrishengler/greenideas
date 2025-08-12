from greenideas.parts_of_speech.pos_types import POSType
from greenideas.rules.expansion_spec import ExpansionSpec
from greenideas.rules.grammar_rule import GrammarRule
from greenideas.rules.source_spec import SourceSpec

# PP -> Prep NP
pp__prep_np = GrammarRule(
    SourceSpec(POSType.PP), [ExpansionSpec(POSType.Prep), ExpansionSpec(POSType.NP)]
)

pp_expansions = [pp__prep_np]
