from greenideas.rules.default_english_rules.attributes.aspect import Aspect
from greenideas.rules.default_english_rules.attributes.default_english_attribute_type import (
    DefaultEnglishAttributeType,
)
from greenideas.rules.default_english_rules.parts_of_speech.default_english_pos_types import (
    DefaultEnglishPOSType,
)
from greenideas.rules.expansion_spec import INHERIT, ExpansionSpec
from greenideas.rules.grammar_rule import GrammarRule
from greenideas.rules.source_spec import SourceSpec

relC__relPron_VP = GrammarRule(
    SourceSpec(DefaultEnglishPOSType.RelClause),
    [
        ExpansionSpec(
            DefaultEnglishPOSType.RelativePron,
            {DefaultEnglishAttributeType.ANIMACY: INHERIT},
        ),
        ExpansionSpec(
            DefaultEnglishPOSType.VP,
            {
                DefaultEnglishAttributeType.ASPECT: [Aspect.SIMPLE],
                DefaultEnglishAttributeType.NUMBER: INHERIT,
                DefaultEnglishAttributeType.PERSON: INHERIT,
            },
        ),
    ],
)

relC_expansions = [
    relC__relPron_VP,
]
