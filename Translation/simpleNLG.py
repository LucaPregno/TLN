from simplenlg import NLGFactory, Realiser
from simplenlg.lexicon import Lexicon
from Translation.model.word import Word, word_list


def example():
    lexicon = Lexicon.getDefaultLexicon()
    nlg_factory = NLGFactory(lexicon)
    realiser = Realiser(lexicon)

    p = nlg_factory.createClause()
    my_dog = nlg_factory.createNounPhrase("dog")
    my_dog.setDeterminer("my")
    p.setSubject(my_dog)
    p.setVerb("chase")
    obj = nlg_factory.createAdjectivePhrase("clean")
    obj.addComplement("car")
    obj.addComplement("bike")
    p.addComplement(obj)
    possession = nlg_factory.createPrepositionPhrase()
    possession.setPreposition("of")
    f = nlg_factory.createNounPhrase("father")
    f.setDeterminer("your")
    possession.addComplement(f)
    p.addComplement(possession)
    print(realiser.realiseSentence(p))


def parse_tree_to_sentence_plan(tree_list):
    lexicon = Lexicon.getDefaultLexicon()
    nlg_factory = NLGFactory(lexicon)
    realiser = Realiser(lexicon)

    for tree in tree_list:
        print("------------------")
        # c = nlg_factory.createClause()
        # define_sentence_plan(c, nlg_factory, tree)


def define_sentence_plan(clause, nlg_factory, tree, phrase=None):

    for subtree in tree.subtrees():

        label = subtree.label()
        value = subtree[0]
        if subtree.label() == "NP":
            print(label, value)
            nlg_factory.createNounPhrase()
        elif subtree.label() == "VP":
            print(label, value)
            v_phrase = nlg_factory.createVerbPhrase()
            for s in subtree.subtrees():
                print("SottoVP", s.label(), s[0])
        elif subtree.label() == "PP":
            print(label, value)
        elif subtree.label() == "NOM":
            print(label, value)
        elif subtree.label() == "PropN":
            print(label, value)
        elif subtree.label() == "Det":
            print(label, value)
        elif subtree.label() == "N":
            print(label, value)
            #nlg_factory.setSub
        elif subtree.label() == "Adj":
            print(label, value)
        elif subtree.label() == "V":
            print(label, value)
        elif subtree.label() == "Aux":
            print(label, value)
        elif subtree.label() == "Adv":
            print(label, value)
        elif subtree.label() == "Prep":
            print(label, value)
        elif subtree.label() == "Adp":
            print(label, value)


def sentence_planning(tree_list):
    lexicon = Lexicon.getDefaultLexicon()
    nlg_factory = NLGFactory(lexicon)
    realiser = Realiser(lexicon)

    for tree in tree_list:
        print("------------")
        pos_tag = tree.pos()
        # matches_verb = (v for v in pos_tag if v[0] == "V")
        # print("m", matches_verb)
        for p in pos_tag:
            if p[1] == "V":
                v = Word(p[0], p[1], pos_tag.index((p[0], p[1])))
                v.print()
            if p[1] == "N":
                n_index_list = [i for i, n in enumerate(pos_tag) if n == "N"]
                n_word_list = word_list(n_index_list, value=p[0], tag=p[1])


