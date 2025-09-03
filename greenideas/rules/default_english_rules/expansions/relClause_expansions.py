from greenideas.attributes.aspect import Aspect
from greenideas.attributes.attribute_type import AttributeType
from greenideas.parts_of_speech.default_english_pos_types import DefaultEnglishPOSType
from greenideas.rules.expansion_spec import INHERIT, ExpansionSpec
from greenideas.rules.grammar_rule import GrammarRule
from greenideas.rules.source_spec import SourceSpec

relC__relPron_VP = GrammarRule(
    SourceSpec(DefaultEnglishPOSType.RelClause),
    [
        ExpansionSpec(
            DefaultEnglishPOSType.RelativePron, {AttributeType.ANIMACY: INHERIT}
        ),
        ExpansionSpec(
            DefaultEnglishPOSType.VP,
            {
                AttributeType.ASPECT: [Aspect.SIMPLE],
                AttributeType.NUMBER: INHERIT,
                AttributeType.PERSON: INHERIT,
            },
        ),
    ],
)

relC_expansions = [
    relC__relPron_VP,
]
