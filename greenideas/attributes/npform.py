from greenideas.attributes.grammatical_attribute import GrammaticalAttribute


# We don't actually want to set a requirement here in most cases so we set free
# with weight 1 and don't let anything else be randomly assigned
# Applying restriction manually is useful in certain rules
class NPForm(GrammaticalAttribute):
    FREE = ("free", 1.0)
    PRONOMINAL = ("pronominal", 0.0)
    LEXICAL = ("lexical", 0.0)
