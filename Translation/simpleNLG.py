from simplenlg import NLGFactory, Realiser
from simplenlg.lexicon import Lexicon


def launch():
    lexicon = Lexicon.getDefaultLexicon()
    nlg_factory = NLGFactory(lexicon)
    realiser = Realiser(lexicon)

