class Object:
    def __init__(self, value="",):
        self.value = value
        self.determiner = []
        self.adjective = []

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
    def __init__(self, value=""):
        self.value = value
        self.obj = Object()

    def print(self):
        self.print_value()
        self.obj.print()

    def print_value(self):
        print("Preposition value", self.value)


class SentencePlan:
    def __init__(self, verb=""):
        self.subject = Object()
        self.verb = verb
        self.object = Object()
        self.preposition = Preposition()

    def print(self):
        print("---Subject---")
        self.print_subj()
        print("---Verb---")
        self.print_verb()
        print("---Object---")
        self.print_obj()

    def print_subj(self):
        self.subject.print()

    def print_verb(self):
        print("Value:", self.verb)

    def print_obj(self):
        self.object.print()
