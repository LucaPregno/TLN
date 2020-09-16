from simplenlg import NLGFactory, Realiser
from simplenlg.lexicon import Lexicon

from Translation.model.father import Father
from Translation.model.sentece_plan import SentencePlan, Object
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
    for tree in tree_list:
        print("------------------")
        sentence_plan = sentence_plan_build(tree)
        # sentence_plan.print()
        launch_simpleNLG(sentence_plan)



def sentence_plan_build(tree):
    sentence_plan = SentencePlan()
    frontier = tree
    len_frontier = len(frontier)
    father = Father(tree.height(), tree.label())
    if len_frontier == 1:
        sentence_plan.subject.value = "It"

    while len_frontier > 0:
        subtree = frontier.pop(0)
        if subtree.label() in ["VP", "PP"]:
            father.set(subtree.height(), subtree.label())
        elif subtree.label() == "NP":
            if father.label == "PP" and subtree.height() < father.height:
                pass
            else:
                father.set(subtree.height(), subtree.label())

        if subtree.label() == "V":
            sentence_plan.verb += subtree[0]
            sentence_plan.verb += " "
        elif subtree.label() == "Aux":
            sentence_plan.verb += subtree[0]
            sentence_plan.verb += " "
        elif subtree.label() == "Adv":
            sentence_plan.verb += subtree[0]
            sentence_plan.verb += " "
        # searching the subject
        if sentence_plan.subject.value == "" and father.label == "NP":
            if subtree.label() == "Det":
                sentence_plan.subject.determiner.append(subtree[0])
            elif subtree.label() == "N":
                sentence_plan.subject.value = subtree[0]
            elif subtree.label() == "Adj":
                sentence_plan.subject.adjective.append(subtree[0])
        # searching the complement
        elif sentence_plan.subject.value != "" and father.label == "NP":
            if subtree.label() == "Det":
                sentence_plan.object.determiner.append(subtree[0])
            if subtree.label() == "N":
                sentence_plan.object.value = subtree[0]
            if subtree.label() == "Adj":
                sentence_plan.object.adjective.append(subtree[0])
        # serching the prepositions
        elif father.label == "PP":
            if subtree.label() == "N":
                sentence_plan.preposition.object.value = subtree[0]
            elif subtree.label() == "Det":
                sentence_plan.preposition.object.determiner.append(subtree[0])
            elif subtree.label() == "PropN":
                sentence_plan.preposition.object.value = subtree[0]
            elif subtree.label() == "Adp":
                sentence_plan.preposition.value = subtree[0]
            elif subtree.label() == "Adj":
                sentence_plan.preposition.object.adjective.append(subtree[0])

        for i in reversed(range(len(subtree))):
            if type(subtree[i]) != str:
                frontier.insert(0, subtree[i])
        len_frontier = len(frontier)

    return sentence_plan


def launch_simpleNLG(sentence_plan):
    lexicon = Lexicon.getDefaultLexicon()
    nlg_factory = NLGFactory(lexicon)
    realiser = Realiser(lexicon)

    c = nlg_factory.createClause()
    NP = nlg_factory.createNounPhrase(sentence_plan.subject.value)
    for d in sentence_plan.subject.determiner:
        NP.setDeterminer(d)
    for a in sentence_plan.subject.adjective:
        NP.addComplement(nlg_factory.createAdjectivePhrase(a))
    c.setSubject(NP)
    c.setVerb(sentence_plan.verb)

    OBJ = nlg_factory.createNounPhrase(sentence_plan.object.value)
    for d in sentence_plan.object.determiner:
        OBJ.setDeterminer(d)
    for a in sentence_plan.subject.adjective:
        OBJ.addComplement(nlg_factory.createAdjectivePhrase(a))
    c.addComplement(OBJ)

    print(realiser.realiseSentence(c))

    # possession = nlg_factory.createPrepositionPhrase()
    # possession.setPreposition("of")
    # f = nlg_factory.createNounPhrase("father")
    # f.setDeterminer("your")
    # possession.addComplement(f)
    # c.addComplement(possession)


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


