from datetime import date, datetime
from math import inf
from person import Person

class interaction:
    def __init__(self, person1, person2):
        self.person1 = Person(person1.vaccinated, person1.infected)
        self.person2 = Person(person2.vaccinated, person2.infected)

    def __repr__(self):
        return f'({self.person1.infected},{self.person1.vaccinated}) interacted with ({self.person2.infected},{self.person2.vaccinated})'


class Logger:
    def __init__(self, name):
        self.interactions = []
        self.file_name = f"{name}_{str(datetime.now())}.txt"
        f = open(self.file_name, "a+")
        f.write(f"{str(datetime.now())} {name}\n\n")
        f.close()

    def log(self, normal_people, vaccinated_people, infected_people, dead_people):
        f = open(self.file_name, "a+")
        f.write("\n")
        f.write(f"{str(datetime.now())}\n")
        f.write(f"\tNormal: {normal_people}, Vaccinated: {vaccinated_people}, Infected: {infected_people}, Dead: {dead_people}\n")
        f.close()

    