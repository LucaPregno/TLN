from simplenlg import NLGFactory, Realiser
from simplenlg.lexicon import Lexicon
from Translation.Model.father import Father
from Translation.Model.sentece_plan import SentencePlan

lexicon = Lexicon.getDefaultLexicon()
nlg_factory = NLGFactory(lexicon)
realiser = Realiser(lexicon)


def parse_tree_to_sentence_plan(tree_list):
    for tree in tree_list:
        sentence_plan = sentence_plan_build(tree)
        use_simplenlg(sentence_plan)
        print("------------------")


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

        # searching something linked to verb
        if father.label == "VP":
            if subtree.label() in ["V", "Aux", "Adv"]:
                sentence_plan.verb.value += subtree[0] + " "
            elif subtree.label() == "NominalPredicate":
                sentence_plan.verb.predicate.append(subtree[0])
        elif father.label == "NP":
            # searching the subject
            if sentence_plan.is_verb_empty():
                if subtree.label() == "Det":
                    sentence_plan.subject.determiner.append(subtree[0])
                elif subtree.label() == "N":
                    sentence_plan.subject.value = subtree[0]
                elif subtree.label() == "Adj":
                    sentence_plan.subject.adjective.append(subtree[0])
            # searching the complement
            elif not sentence_plan.is_verb_empty():
                if subtree.label() == "Det":
                    sentence_plan.object.determiner.append(subtree[0])
                if subtree.label() == "N":
                    sentence_plan.object.value = subtree[0]
                if subtree.label() == "Adj":
                    sentence_plan.object.adjective.append(subtree[0])
        elif father.label == "PP":
            # searching the prepositions referring to subject
            if sentence_plan.is_verb_empty():
                if subtree.label() in ["N", "PropN"]:
                    sentence_plan.subject.preposition.object = subtree[0]
                elif subtree.label() == "Det":
                    sentence_plan.subject.preposition.determiner.append(subtree[0])
                elif subtree.label() == "Adp":
                    sentence_plan.subject.preposition.value = subtree[0]
                elif subtree.label() == "Adj":
                    sentence_plan.subject.preposition.adjective.append(subtree[0])
            # searching the prepositions referring to complement
            elif not sentence_plan.is_verb_empty():
                if subtree.label() in ["N", "PropN"]:
                    sentence_plan.object.preposition.object = subtree[0]
                elif subtree.label() == "Det":
                    sentence_plan.object.preposition.determiner.append(subtree[0])
                elif subtree.label() == "Adp":
                    sentence_plan.object.preposition.value = subtree[0]
                elif subtree.label() == "Adj":
                    sentence_plan.object.preposition.adjective.append(subtree[0])

        for i in reversed(range(len(subtree))):
            if type(subtree[i]) != str:
                frontier.insert(0, subtree[i])
        len_frontier = len(frontier)

    return sentence_plan


def use_simplenlg(sentence_plan):
    c = nlg_factory.createClause()
    np = realiser_object(sentence_plan.subject)
    c.setSubject(np)
    vp = realiser_verb(sentence_plan.verb)
    c.setVerb(vp)
    complement = realiser_object(sentence_plan.object)
    c.addComplement(complement)
    print(realiser.realiseSentence(c))


def realiser_object(obj):
    np = nlg_factory.createNounPhrase(obj.value)
    for d in obj.determiner:
        np.setDeterminer(d)
    for a in obj.adjective:
        np.addModifier(a)
    # if there is some preposition referenced to obj
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


def realiser_verb(verb):
    vp = nlg_factory.createVerbPhrase(verb.value)
    for p in verb.predicate:
        vp.addModifier(p)
    return vp
