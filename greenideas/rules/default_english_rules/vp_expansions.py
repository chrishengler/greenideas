from greenideas.attributes.attribute_type import AttributeType
from greenideas.attributes.case import Case
from greenideas.attributes.npform import NPForm
from greenideas.attributes.person import Person
from greenideas.attributes.valency import Valency
from greenideas.attributes.voice import Voice
from greenideas.parts_of_speech.pos_types import POSType
from greenideas.rules.expansion_spec import INHERIT, ExpansionSpec
from greenideas.rules.grammar_rule import GrammarRule
from greenideas.rules.source_spec import SourceSpec

# VP -> VP AdvP
vp__vp_advp = GrammarRule(
    SourceSpec(POSType.VP),
    [
        ExpansionSpec(
            POSType.VP,
            {
                AttributeType.ASPECT: INHERIT,
                AttributeType.NUMBER: INHERIT,
                AttributeType.TENSE: INHERIT,
                AttributeType.PERSON: INHERIT,
                AttributeType.VALENCY: INHERIT,
                AttributeType.VOICE: INHERIT,
            },
        ),
        ExpansionSpec(POSType.AdvP),
    ],
    weight=0.2,
)

# VP1 -> V1
vp1__v = GrammarRule(
    SourceSpec(
        POSType.VP,
        {
            AttributeType.VALENCY: Valency.MONOVALENT,
            AttributeType.VOICE: Voice.ACTIVE,
        },
    ),
    [
        ExpansionSpec(
            POSType.Verb,
            {
                AttributeType.ASPECT: INHERIT,
                AttributeType.NUMBER: INHERIT,
                AttributeType.TENSE: INHERIT,
                AttributeType.PERSON: INHERIT,
                AttributeType.VALENCY: INHERIT,
                AttributeType.VOICE: INHERIT,
            },
        ),
    ],
)

# VP2 -> V NP.Obj
vp2__v_npAcc = GrammarRule(
    SourceSpec(
        POSType.VP,
        {
            AttributeType.VALENCY: Valency.DIVALENT,
            AttributeType.VOICE: Voice.ACTIVE,
        },
    ),
    [
        ExpansionSpec(
            POSType.Verb,
            {
                AttributeType.ASPECT: INHERIT,
                AttributeType.NUMBER: INHERIT,
                AttributeType.TENSE: INHERIT,
                AttributeType.PERSON: INHERIT,
                AttributeType.VALENCY: INHERIT,
                AttributeType.VOICE: INHERIT,
            },
        ),
        ExpansionSpec(
            POSType.NP,
            {
                AttributeType.CASE: Case.OBJECTIVE,
            },
        ),
    ],
)

# VP3 -> V NP.Obj NP.Obj
vp3__v_npAcc_npNom = GrammarRule(
    SourceSpec(
        POSType.VP,
        {AttributeType.VALENCY: Valency.TRIVALENT, AttributeType.VOICE: Voice.ACTIVE},
    ),
    [
        ExpansionSpec(
            POSType.Verb,
            {
                AttributeType.ASPECT: INHERIT,
                AttributeType.NUMBER: INHERIT,
                AttributeType.TENSE: INHERIT,
                AttributeType.PERSON: INHERIT,
                AttributeType.VALENCY: INHERIT,
                AttributeType.VOICE: INHERIT,
            },
        ),
        ExpansionSpec(
            POSType.NP,
            {
                AttributeType.NPFORM: NPForm.PRONOMINAL,
                AttributeType.CASE: Case.OBJECTIVE,
            },
        ),
        ExpansionSpec(
            POSType.NP,
            {
                AttributeType.NPFORM: NPForm.LEXICAL,
                AttributeType.CASE: Case.OBJECTIVE,
                AttributeType.PERSON: Person.THIRD,
            },
        ),
    ],
)


# VP -> VP PP
vp__vp_pp = GrammarRule(
    SourceSpec(POSType.VP),
    [
        ExpansionSpec(
            POSType.VP,
            {
                AttributeType.ASPECT: INHERIT,
                AttributeType.NUMBER: INHERIT,
                AttributeType.TENSE: INHERIT,
                AttributeType.PERSON: INHERIT,
                AttributeType.VALENCY: INHERIT,
                AttributeType.VOICE: INHERIT,
            },
        ),
        ExpansionSpec(POSType.PP),
    ],
    weight=0.2,
)

# VP -> VP Conj VP
vp__vp_conj_vp = GrammarRule(
    SourceSpec(POSType.VP),
    [
        ExpansionSpec(
            POSType.VP,
            {
                AttributeType.ASPECT: INHERIT,
                AttributeType.NUMBER: INHERIT,
                AttributeType.TENSE: INHERIT,
                AttributeType.PERSON: INHERIT,
                AttributeType.VALENCY: INHERIT,
                AttributeType.VOICE: INHERIT,
            },
        ),
        ExpansionSpec(POSType.SimpleConj),
        ExpansionSpec(
            POSType.VP,
            {
                AttributeType.ASPECT: INHERIT,
                AttributeType.NUMBER: INHERIT,
                AttributeType.TENSE: INHERIT,
                AttributeType.PERSON: INHERIT,
                AttributeType.VOICE: INHERIT,
            },
        ),
    ],
    weight=0.2,
)

# vp_passive -> VP_Passive
vp_pass__vpPass = GrammarRule(
    SourceSpec(POSType.VP, {AttributeType.VOICE: Voice.PASSIVE}),
    [
        ExpansionSpec(
            POSType.VP_Passive,
            {
                AttributeType.ASPECT: INHERIT,
                AttributeType.NUMBER: INHERIT,
                AttributeType.TENSE: INHERIT,
                AttributeType.PERSON: INHERIT,
            },
        )
    ],
)


vp_expansions = [
    vp__vp_advp,
    vp__vp_pp,
    vp__vp_conj_vp,
    vp1__v,
    vp2__v_npAcc,
    vp3__v_npAcc_npNom,
    vp_pass__vpPass,
]
