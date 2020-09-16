from simplenlg import NLGFactory, Realiser
from simplenlg.lexicon import Lexicon

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
    lexicon = Lexicon.getDefaultLexicon()
    nlg_factory = NLGFactory(lexicon)
    realiser = Realiser(lexicon)

    # define_sentence_plan(tree_list[2], SentencePlan())

    for tree in tree_list:
        print("------------------")
        # define_sentence_plan(tree)
        sentence_plan = SentencePlan()
        s = deep_search(tree, sentence_plan)
        s.print()


def define_sentence_plan(tree):
    pass
    # sentence_plan = SentencePlan()
    # root_h = tree.height()
    # print("root", root_h)
    # if there is no subject force it to "It"
    # if len(tree) == 1:
    #     sentence_plan.subj = "It"

    # for subtree in tree.subtrees():
    #     n_subtree = len(subtree)
    #     label = subtree.label()
    #     value = subtree[0]
    #     h = subtree.height()
    #     print("label", subtree.label(), "value", value, "h", h)
    #     if subtree.label() == "NP":
    #         # If there is a subject in the sentence
    #         #AGGIUNGO AL SOGGETTO
    #         if sentence_plan.subject != "":
    #             print(label, value)
    #             if subtree.label() == "Det":
    #                 print(label, value)
    #             elif subtree.label() == "N":
    #                 print(label, value)
    #             elif subtree.label() == "Adj":
    #                 print(label, value)
    #         else: # AGGIUNGO PP
    #             if subtree.label() == "Det":
    #                 print(label, value)
    #             elif subtree.label() == "N":
    #                 print(label, value)
    #             elif subtree.label() == "Adj":
    #                 print(label, value)
    #
    #     elif subtree.label() == "VP":
    #         # COMPLEMENTO OGGETTO
    #         print(label, value, h)
    #         # for s in subtree.subtrees():
    #         #     print("SottoVP", s.label(), s[0])
    #     elif subtree.label() == "PP":
    #         print(label, value)
    #     elif subtree.label() == "NOM":
    #         print(label, value)
    #     elif subtree.label() == "PropN":
    #         print(label, value)
    #     elif subtree.label() == "Adp":
    #         print(label, value)
    #     elif subtree.label() == "V":
    #         sentence_plan.verb += value
    #         sentence_plan.verb += " "
    #     elif subtree.label() == "Aux":
    #         sentence_plan.verb += value
    #         sentence_plan.verb += " "
    #     elif subtree.label() == "Adv":
    #         sentence_plan.verb += value
    #         sentence_plan.verb += " "
    #
    # print("--------------------")
    # sentence_plan.print()


def deep_search(tree, sentence_plan):
    frontier = tree
    len_frontier = len(frontier)
    if len_frontier == 1:
        sentence_plan.subject.value = "It"

    while len_frontier > 0:
        # print("len_frontier", len_frontier)
        # print("frontier", frontier)
        # print("label", subtree.label(), "value", subtree)
        subtree = frontier.pop()
        if subtree.label() == "V":
            sentence_plan.verb += subtree[0]
            sentence_plan.verb += " "
        elif subtree.label() == "Aux":
            sentence_plan.verb += subtree[0]
            sentence_plan.verb += " "
        elif subtree.label() == "Adv":
            sentence_plan.verb += subtree[0]
            sentence_plan.verb += " "
        elif sentence_plan.subject.value == "" and subtree.label() != "PP":
            if subtree.label() == "Det":
                sentence_plan.subject.determiner.append(subtree[0])
            elif subtree.label() == "N":
                sentence_plan.subject.value = subtree[0]
            elif subtree.label() == "Adj":
                sentence_plan.subject.adjective.append(subtree[0])
        elif sentence_plan.subject.value != "" and subtree.label() != "PP":
            if subtree.label() == "Det":
                sentence_plan.object.determiner.append(subtree[0])
            elif subtree.label() == "N":
                sentence_plan.object.value = subtree[0]
            elif subtree.label() == "Adj":
                sentence_plan.object.adjective.append(subtree[0])

        for i in reversed(range(len(subtree))):
            if type(subtree[i]) != str:
                # print("child", i, "type", type(subtree), subtree[i])
                frontier.insert(0, subtree[i])
        len_frontier = len(frontier)

    return sentence_plan


def launch_simpleNLG():
    lexicon = Lexicon.getDefaultLexicon()
    nlg_factory = NLGFactory(lexicon)
    realiser = Realiser(lexicon)

    sentence_plan = SentencePlan()
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


