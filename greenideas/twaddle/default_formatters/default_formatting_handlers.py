from greenideas.rules.default_english_rules.parts_of_speech.default_english_pos_types import (
    DefaultEnglishPOSType,
)
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
from greenideas.twaddle.default_formatters.deg_formatting_handler import (
    DegFormattingHandler,
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
from greenideas.twaddle.default_formatters.simpleconj_formatting_handler import (
    SimpleConjFormattingHandler,
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

default_formatting_handlers: dict[DefaultEnglishPOSType, TwaddleFormattingHandler] = {
    DefaultEnglishPOSType.Adj: AdjFormattingHandler,
    DefaultEnglishPOSType.Adv: AdvFormattingHandler,
    DefaultEnglishPOSType.Aux_do: AuxDoFormattingHandler,
    DefaultEnglishPOSType.Aux_finite: AuxFiniteFormattingHandler,
    DefaultEnglishPOSType.Be: BeFormattingHandler,
    DefaultEnglishPOSType.CoordConj: CoordconjFormattingHandler,
    DefaultEnglishPOSType.Deg: DegFormattingHandler,
    DefaultEnglishPOSType.Det: DetFormattingHandler,
    DefaultEnglishPOSType.Modal: ModalFormattingHandler,
    DefaultEnglishPOSType.Noun: NounFormattingHandler,
    DefaultEnglishPOSType.Prep: PrepFormattingHandler,
    DefaultEnglishPOSType.Pron: PronFormattingHandler,
    DefaultEnglishPOSType.RelativePron: RelativePronounFormattingHandler,
    DefaultEnglishPOSType.SimpleConj: SimpleConjFormattingHandler,
    DefaultEnglishPOSType.Subordinator: SubordinatorFormattingHandler,
    DefaultEnglishPOSType.Verb: VerbFormattingHandler,
    DefaultEnglishPOSType.Verb_AfterModal: VerbAfterModalFormattingHandler,
    DefaultEnglishPOSType.Verb_Bare: VerbBareFormattingHandler,
}
