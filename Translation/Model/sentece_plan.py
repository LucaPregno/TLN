class Object:
    def __init__(self, value=""):
        self.value = value
        self.determiner = []
        self.adjective = []
        self.preposition = Preposition()

    def print(self):
        self.print_value()
        self.print_determiner()
        self.print_adjective()
        self.preposition.print()

    def print_value(self):
        print("Value:", self.value)

    def print_determiner(self):
        print("Determiner:", self.determiner)

    def print_adjective(self):
        print("Adjective:", self.adjective)


class Verb:
    def __init__(self, value=""):
        self.value = value
        self.predicate = []

    def print(self):
        self.print_value()
        self.print_predicate()

    def print_value(self):
        print("Value:", self.value)

    def print_predicate(self):
        print("Predicate:", self.predicate)


class Preposition:
    def __init__(self, value=""):
        self.value = value
        self.object = ""
        self.determiner = []
        self.adjective = []

    def print(self):
        print("-Preposition-")
        self.print_value()
        self.print_object()
        self.print_determiner()
        self.print_adjective()

    def print_value(self):
        print("Preposition value:", self.value)

    def print_object(self):
        print("Object:", self.object)

    def print_determiner(self):
        print("Determiner:", self.determiner)

    def print_adjective(self):
        print("Adjective:", self.adjective)


class SentencePlan:
    def __init__(self):
        self.subject = Object()
        self.verb = Verb()
        self.object = Object()

    def print(self):
        print("---Subject---")
        self.print_subject()
        print("---Verb---")
        self.print_verb()
        print("---Object---")
        self.print_object()

    def print_subject(self):
        self.subject.print()

    def print_verb(self):
        self.verb.print()

    def print_object(self):
        self.object.print()

    def is_verb_empty(self) -> bool:
        return True if self.verb.value == "" else False
