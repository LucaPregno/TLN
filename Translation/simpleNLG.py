from simplenlg import NLGFactory, Realiser
from simplenlg.lexicon import Lexicon

from Translation.model.father import Father
from Translation.model.sentece_plan import SentencePlan, Object
from Translation.model.word import Word, word_list

lexicon = Lexicon.getDefaultLexicon()
nlg_factory = NLGFactory(lexicon)
realiser = Realiser(lexicon)

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
            sentence_plan.verb += str(subtree[0])
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
        # searching the prepositions referring to subject
        elif father.label == "PP" and sentence_plan.subject.value != ("" or "It"):
            if subtree.label() == "N":
                sentence_plan.subject.preposition.object = subtree[0]
            elif subtree.label() == "Det":
                sentence_plan.subject.preposition.determiner.append(subtree[0])
            elif subtree.label() == "PropN":
                sentence_plan.subject.preposition.object = subtree[0]
            elif subtree.label() == "Adp":
                sentence_plan.subject.preposition.value = subtree[0]
            elif subtree.label() == "Adj":
                sentence_plan.subject.preposition.adjective.append(subtree[0])
        # searching the prepositions referring to complement
        elif father.label == "PP" and sentence_plan.object.value != "":
            if subtree.label() == "N":
                sentence_plan.object.preposition.object = subtree[0]
            elif subtree.label() == "Det":
                sentence_plan.object.preposition.determiner.append(subtree[0])
            elif subtree.label() == "PropN":
                sentence_plan.object.preposition.object = subtree[0]
            elif subtree.label() == "Adp":
                sentence_plan.object.preposition.value = subtree[0]
            elif subtree.label() == "Adj":
                sentence_plan.object.preposition.adjective.append(subtree[0])

        for i in reversed(range(len(subtree))):
            if type(subtree[i]) != str:
                frontier.insert(0, subtree[i])
        len_frontier = len(frontier)

    return sentence_plan


def launch_simpleNLG(sentence_plan):
    c = nlg_factory.createClause()
    # np = nlg_factory.createNounPhrase(sentence_plan.subject.value)
    # for d in sentence_plan.subject.determiner:
    #     np.setDeterminer(d)
    # for a in sentence_plan.subject.adjective:
    #     np.addModifier(a)
    np = realizer_object(sentence_plan.subject)
    c.setSubject(np)
    c.setVerb(sentence_plan.verb)
    # complement = nlg_factory.createNounPhrase(sentence_plan.object.value)
    # for d in sentence_plan.object.determiner:
    #     complement.setDeterminer(d)
    # for a in sentence_plan.object.adjective:
    #     complement.addModifier(a)
    complement = realizer_object(sentence_plan.object)
    c.addComplement(complement)

    print(realiser.realiseSentence(c))


def realizer_object(obj):
    obj.print()
    np = nlg_factory.createNounPhrase(obj.value)
    for d in obj.determiner:
        np.setDeterminer(d)
    for a in obj.adjective:
        np.addModifier(a)

    if obj.preposition.value != "":
        preposition = nlg_factory.createPrepositionPhrase()
        preposition.setPreposition(obj.preposition.value)
        p_np = nlg_factory.createNounPhrase(obj.preposition.object)
        for d in obj.preposition.determiner:
            p_np.setDeterminer(d)
        for a in obj.preposition.adjective:
            p_np.addModifier(a)
        preposition.addComplement(p_np)
        np.addComplement(preposition)

    return np


def sentence_planning(tree_list):
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


