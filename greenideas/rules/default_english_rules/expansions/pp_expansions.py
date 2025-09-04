from greenideas.rules.default_english_rules.attributes.case import Case
from greenideas.rules.default_english_rules.attributes.default_english_attribute_type import (
    DefaultEnglishAttributeType,
)
from greenideas.rules.default_english_rules.parts_of_speech.default_english_pos_types import (
    DefaultEnglishPOSType,
)
from greenideas.rules.expansion_spec import ExpansionSpec
from greenideas.rules.grammar_rule import GrammarRule
from greenideas.rules.source_spec import SourceSpec

# PP -> Prep NP
pp__prep_np = GrammarRule(
    SourceSpec(DefaultEnglishPOSType.PP),
    [
        ExpansionSpec(DefaultEnglishPOSType.Prep),
        ExpansionSpec(
            DefaultEnglishPOSType.NP, {DefaultEnglishAttributeType.CASE: Case.OBJECTIVE}
        ),
    ],
)

pp_expansions = [pp__prep_np]
