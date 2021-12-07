from datetime import date, datetime
from math import inf
from time import sleep
from person import Person

class interaction:
    def __init__(self, person1, person2):
        self.person1 = Person(person1.vaccinated, person1.infected)
        self.person2 = Person(person2.vaccinated, person2.infected)

    def __repr__(self):
        return f'({self.person1.infected},{self.person1.vaccinated}) interacted with ({self.person2.infected},{self.person2.vaccinated})'


class Logger:
    def __init__(self, virus, pop_size, vac_perc, init_infected):
        #starting values
        self.pop_size = pop_size
        self.vac_perc = vac_perc
        self.init_infected = init_infected

        self.total_infected = 0
        self.dead_people = 0
        self.saved_people = 0

        self.file_name = f"{virus.name}_{str(datetime.now())}.txt"
        f = open(self.file_name, "a+")
        f.write(f"{str(datetime.now())} {virus.name}\n")
        f.write(f"Population size: {pop_size}, percent vaccinated: {vac_perc}, virus name: {virus.name}, mortality rate: {virus.mort_rate}, reproductive rate: {virus.rep_rate}\n\n")
        f.close()

    def log(self, normal_people, vaccinated_people, infected_people, dead_people, saved_people):
        self.total_infected += infected_people
        self.dead_people = dead_people
        self.saved_people += saved_people

        f = open(self.file_name, "a+")
        f.write("\n")
        f.write(f"{str(datetime.now())}\n")
        f.write(f"\tNormal: {normal_people}, Vaccinated: {vaccinated_people}, Infected: {infected_people}, Dead: {dead_people}\n")
        f.close()

    def log_questions(self):
        f = open(self.file_name, "a+")
        f.write("\n")

        #question 2
        f.write("\n")
        f.write("What percentage of the population became infected at some point before the virus burned out?\n")
        f.write(f"\t{self.total_infected/self.pop_size*100}% of the population was infected\n")

        #question 3
        f.write("\n")
        f.write("What percentage of the population died from the virus?\n")
        f.write(f"\t{self.dead_people/self.pop_size*100}% of the population died to the virus\n")

        #question 4
        f.write("\n")
        f.write("Out of all interactions sick individuals had during the entire simulation, how many total interactions did we see where a vaccination saved a person from potentially becoming infected?\n")
        f.write(f"\t{self.saved_people} people were saved by being vaccinated\n")

        f.close()

    