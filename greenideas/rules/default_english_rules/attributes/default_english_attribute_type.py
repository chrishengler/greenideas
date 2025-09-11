from typing import Type

from greenideas.attributes.attribute_type import AttributeType
from greenideas.rules.default_english_rules.attributes.animacy import Animacy
from greenideas.rules.default_english_rules.attributes.aspect import Aspect
from greenideas.rules.default_english_rules.attributes.case import Case
from greenideas.rules.default_english_rules.attributes.mood import Mood
from greenideas.rules.default_english_rules.attributes.npform import NPForm
from greenideas.rules.default_english_rules.attributes.number import Number
from greenideas.rules.default_english_rules.attributes.person import Person
from greenideas.rules.default_english_rules.attributes.tense import Tense
from greenideas.rules.default_english_rules.attributes.valency import Valency
from greenideas.rules.default_english_rules.attributes.voice import Voice


class DefaultEnglishAttributeType(AttributeType):
    ASPECT = ("aspect", Aspect)
    ANIMACY = ("animacy", Animacy)
    CASE = ("case", Case)
    MOOD = ("mood", Mood)
    NPFORM = ("NPform", NPForm)
    NUMBER = ("number", Number)
    PERSON = ("person", Person)
    TENSE = ("tense", Tense)
    VALENCY = ("valency", Valency)
    VOICE = ("voice", Voice)

    def __init__(self, attr_name: str, value_type: Type):
        super().__init__(attr_name, value_type)
