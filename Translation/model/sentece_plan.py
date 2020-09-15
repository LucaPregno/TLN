from enum import Enum


class SentencePlan:
    def __init__(self, subj, verb, obj, preposition):
        self.subj = subj
        self.verb = verb
        self.obj = obj
        self.preposition = preposition

    def print(self):
        print(self.print_subj(), self.print_verb(), self.print_obj())

    def print_subj(self):
        print("Subject:", self.subj)

    def print_verb(self):
        print("Verb:", self.verb)

    def print_obj(self):
        print("Object:", self.obj)


class Preposition:
    def __init__(self, value, reference):
        self.value = value
        self.reference = reference

    def print(self):
        print("Preposition:", self.value, "reference:", self.reference)


class Reference(Enum):
    SUBJ = 0
    VERB = 1
    OBJ = 2
