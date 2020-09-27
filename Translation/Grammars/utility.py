from nltk import load
from nltk.grammar import is_terminal

grammar_url = "file:/grammars/grammar.cfg"


def set_grammar_url(new_grammar):
    global grammar_url
    grammar_url = new_grammar


def print_grammar_rules(grammar=load(grammar_url)):
    print("Grammar Rules")
    for p in grammar.productions():
        print("Right hand side production", p.rhs())
        print("Left hand side production", p.lhs())
        print(p)


def get_lhs_terminal(grammar=load(grammar_url)):
    """
    Return a production list of lhs(left hand side) that are terminal
    :param grammar:
    :return:
    """
    lhs_list = []
    for p in grammar.productions():
        if p.lhs() not in lhs_list and is_terminal(p.rhs()[0]):
            lhs_list.append(p.lhs())
    return lhs_list
