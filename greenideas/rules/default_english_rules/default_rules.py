from greenideas.rules.default_english_rules.expansions.adjP_expansions import (
    adjP_expansions,
)
from greenideas.rules.default_english_rules.expansions.advP_expansions import (
    advP_expansions,
)
from greenideas.rules.default_english_rules.expansions.auxP_expansions import (
    auxP_expansions,
)
from greenideas.rules.default_english_rules.expansions.modalP_expansions import (
    modalP_expansions,
)
from greenideas.rules.default_english_rules.expansions.np_expansions import (
    np_expansions,
)
from greenideas.rules.default_english_rules.expansions.npNodet_expansions import (
    npNodet_expansions,
)
from greenideas.rules.default_english_rules.expansions.pp_expansions import (
    pp_expansions,
)
from greenideas.rules.default_english_rules.expansions.q_expansions import (
    question_expansions,
)
from greenideas.rules.default_english_rules.expansions.relClause_expansions import (
    relC_expansions,
)
from greenideas.rules.default_english_rules.expansions.s_expansions import s_expansions
from greenideas.rules.default_english_rules.expansions.utterance_expansions import (
    u_expansions,
)
from greenideas.rules.default_english_rules.expansions.vp_expansions import (
    vp_expansions,
)
from greenideas.rules.default_english_rules.expansions.vpAfterFrontedAux_expansions import (
    vpAfterFA_expansions,
)
from greenideas.rules.default_english_rules.expansions.vpAfterModal_expansions import (
    vpAfterModal_expansions,
)
from greenideas.rules.default_english_rules.expansions.vpBare_expansions import (
    vpBare_expansions,
)
from greenideas.rules.default_english_rules.expansions.vpPassive_expansions import (
    vp_passive_expansions,
)
from greenideas.rules.default_english_rules.parts_of_speech.default_english_pos_attributes import (
    relevant_attributes,
)
from greenideas.rules.grammar_ruleset import GrammarRuleset

default_rules = GrammarRuleset(pos_attribute_relevance=relevant_attributes)


default_rules.add_rules(u_expansions)
default_rules.add_rules(s_expansions)
default_rules.add_rules(adjP_expansions)
default_rules.add_rules(advP_expansions)
default_rules.add_rules(auxP_expansions)
default_rules.add_rules(modalP_expansions)
default_rules.add_rules(np_expansions)
default_rules.add_rules(npNodet_expansions)
default_rules.add_rules(pp_expansions)
default_rules.add_rules(question_expansions)
default_rules.add_rules(relC_expansions)
default_rules.add_rules(vp_expansions)
default_rules.add_rules(vpAfterFA_expansions)
default_rules.add_rules(vpAfterModal_expansions)
default_rules.add_rules(vpBare_expansions)
default_rules.add_rules(vp_passive_expansions)
