from greenideas.parts_of_speech.pos_types import POSType
from greenideas.twaddle.default_formatters.adj_formatting_handler import (
    AdjFormattingHandler,
)
from greenideas.twaddle.default_formatters.adv_formatting_handler import (
    AdvFormattingHandler,
)
from greenideas.twaddle.default_formatters.aux_do_formatting_handler import (
    AuxDoFormattingHandler,
)
from greenideas.twaddle.default_formatters.aux_finite_formatting_handler import (
    AuxFiniteFormattingHandler,
)
from greenideas.twaddle.default_formatters.be_formatting_handler import (
    BeFormattingHandler,
)
from greenideas.twaddle.default_formatters.coordconj_formatting_handler import (
    CoordconjFormattingHandler,
)
from greenideas.twaddle.default_formatters.det_formatting_handler import (
    DetFormattingHandler,
)
from greenideas.twaddle.default_formatters.modal_formatting_handler import (
    ModalFormattingHandler,
)
from greenideas.twaddle.default_formatters.noun_formatting_handler import (
    NounFormattingHandler,
)
from greenideas.twaddle.default_formatters.prep_formatting_handler import (
    PrepFormattingHandler,
)
from greenideas.twaddle.default_formatters.pron_formatting_handler import (
    PronFormattingHandler,
)
from greenideas.twaddle.default_formatters.relative_pronoun_formatting_handler import (
    RelativePronounFormattingHandler,
)
from greenideas.twaddle.default_formatters.subordinator_formatting_handler import (
    SubordinatorFormattingHandler,
)
from greenideas.twaddle.default_formatters.verb_after_modal_formatting_handler import (
    VerbAfterModalFormattingHandler,
)
from greenideas.twaddle.default_formatters.verb_bare_formatting_handler import (
    VerbBareFormattingHandler,
)
from greenideas.twaddle.default_formatters.verb_formatting_handler import (
    VerbFormattingHandler,
)
from greenideas.twaddle.twaddle_formatting_handler import TwaddleFormattingHandler

default_formatting_handlers: dict[POSType, TwaddleFormattingHandler] = {
    POSType.Adj: AdjFormattingHandler,
    POSType.Adv: AdvFormattingHandler,
    POSType.Aux_do: AuxDoFormattingHandler,
    POSType.Aux_finite: AuxFiniteFormattingHandler,
    POSType.Be: BeFormattingHandler,
    POSType.CoordConj: CoordconjFormattingHandler,
    POSType.Det: DetFormattingHandler,
    POSType.Modal: ModalFormattingHandler,
    POSType.Noun: NounFormattingHandler,
    POSType.Prep: PrepFormattingHandler,
    POSType.Pron: PronFormattingHandler,
    POSType.RelativePron: RelativePronounFormattingHandler,
    POSType.Subordinator: SubordinatorFormattingHandler,
    POSType.Verb: VerbFormattingHandler,
    POSType.Verb_AfterModal: VerbAfterModalFormattingHandler,
    POSType.Verb_Bare: VerbBareFormattingHandler,
}
