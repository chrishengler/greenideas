from greenideas.parts_of_speech.pos_types import POSType
from greenideas.twaddle.default_formatters.adj_formatting_handler import (
    AdjFormattingHandler,
)
from greenideas.twaddle.default_formatters.adv_formatting_handler import (
    AdvFormattingHandler,
)
from greenideas.twaddle.default_formatters.det_formatting_handler import (
    DetFormattingHandler,
)
from greenideas.twaddle.default_formatters.noun_formatting_handler import (
    NounFormattingHandler,
)
from greenideas.twaddle.default_formatters.prep_formatting_handler import (
    PrepFormattingHandler,
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
    POSType.Det: DetFormattingHandler,
    POSType.Noun: NounFormattingHandler,
    POSType.Prep: PrepFormattingHandler,
    POSType.Verb: VerbFormattingHandler,
    POSType.Verb_Bare: VerbBareFormattingHandler,
}
