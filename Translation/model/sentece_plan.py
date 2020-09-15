from enum import Enum


class Object:
    def __init__(self, value="", determiner=[], adjective=[]):
        self.value = value
        self.determiner = determiner
        self.adjective = adjective

    def print(self):
        self.print_value()
        self.print_determiner()
        self.print_adjective()

    def print_value(self):
        print("Value:", self.value)

    def print_determiner(self):
        print("Determiner:", self.determiner)

    def print_adjective(self):
        print("Adjective:", self.adjective)


class Preposition:
    def __init__(self, value, obj=Object()):
        self.value = value
        self.obj = obj

    def print(self):
        self.print_value()
        self.obj.print()

    def print_value(self):
        print("Preposition value", self.value)


class SentencePlan:
    def __init__(self, subj=Object(), verb="", obj=Object(), preposition=None):
        self.subj = subj
        self.verb = verb
        self.obj = obj
        self.preposition = preposition

    def print(self):
        self.print_subj()
        self.print_verb()
        self.print_obj()

    def print_subj(self):
        print("Subject:", self.subj)

    def print_verb(self):
        print("Verb:", self.verb)

    def print_obj(self):
        print("Object:", self.obj)
