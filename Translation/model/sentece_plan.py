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
    def __init__(self, value="", obj=Object()):
        self.value = value
        self.obj = obj

    def print(self):
        self.print_value()
        self.obj.print()

    def print_value(self):
        print("Preposition value", self.value)


class SentencePlan:
    def __init__(self, subj=Object(), obj=Object(), verb="", preposition=Preposition()):
        self.subject = subj
        self.verb = verb
        self.obj = obj
        self.preposition = preposition

    def print(self):
        self.subject.print()
        self.print_verb()
        self.obj.print()

    def print_subj(self):
        self.subject.print()

    def print_verb(self):
        print("Verb:", self.verb)

    def print_obj(self):
        self.obj.print()
