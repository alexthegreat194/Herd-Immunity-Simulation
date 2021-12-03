
from person import Person

class interaction:
    def __init__(self, person1, person2):
        self.person1 = Person(person1.vaccinated, person1.infected)
        self.person2 = Person(person2.vaccinated, person2.infected)

    def __repr__(self):
        return f'({self.person1.infected},{self.person1.vaccinated}) interacted with ({self.person2.infected},{self.person2.vaccinated})'


class Logger:
    def __init__(self):
        self.interactions = []