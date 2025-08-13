from greenideas.attributes.attribute_type import AttributeType
from greenideas.attributes.case import Case
from greenideas.parts_of_speech.pos_types import POSType
from greenideas.rules.expansion_spec import ExpansionSpec
from greenideas.rules.grammar_rule import GrammarRule
from greenideas.rules.source_spec import SourceSpec

# PP -> Prep NP
pp__prep_np = GrammarRule(
    SourceSpec(POSType.PP),
    [
        ExpansionSpec(POSType.Prep),
        ExpansionSpec(POSType.NP, {AttributeType.CASE: Case.OBJECTIVE}),
    ],
)

pp_expansions = [pp__prep_np]
