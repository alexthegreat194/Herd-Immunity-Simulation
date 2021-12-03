from enum import Enum

class State(Enum):
    NORMAL = 0
    INFECTED = 1
    VACCINATED = 2
    DEAD = 3

class Person:
    def __init__(self, vaccinated=False, infected=False):
        self.vaccinated = vaccinated
        self.infected = infected
        self.dead = False
