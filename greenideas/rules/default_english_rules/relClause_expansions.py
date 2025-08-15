from greenideas.attributes.aspect import Aspect
from greenideas.attributes.attribute_type import AttributeType
from greenideas.parts_of_speech.pos_types import POSType
from greenideas.rules.expansion_spec import INHERIT, ExpansionSpec
from greenideas.rules.grammar_rule import GrammarRule
from greenideas.rules.source_spec import SourceSpec

relC__relPron_VP = GrammarRule(
    SourceSpec(POSType.RelClause),
    [
        ExpansionSpec(POSType.RelativePron, {AttributeType.ANIMACY: INHERIT}),
        ExpansionSpec(
            POSType.VP,
            {
                AttributeType.ASPECT: [Aspect.SIMPLE, Aspect.PERFECT],
            },
        ),
    ],
)

relC_expansions = [
    relC__relPron_VP,
]
