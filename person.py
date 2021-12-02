from enum import Enum

class State(Enum):
    NORMAL = 0
    INFECTED = 1
    VACCINATED = 2
    DEAD = 3

class Person:
    def __init__(self, state=State.NORMAL):
        self.state = state
