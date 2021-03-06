import random
import sys
from person import Person, State
from virus import Virus
from logger import Logger
from time import sleep, time

'''
TODO:
make logger class 
'''

class Simulation:
    def __init__(self, pop_size, vac_perc, virus_name, rep_rate, mort_rate, init_infected):
        #create virus
        self.virus = Virus(virus_name, rep_rate, mort_rate)
        
        #create logger
        self.logger = Logger(self.virus, pop_size, vac_perc, init_infected)
        
        #create people
        self.people = []
        for i in range(pop_size):
            self.people.append(Person())
        
        #give vaccines
        for i in range(int(pop_size * vac_perc)):
            self.people[i].vaccinated = True
        random.shuffle(self.people)

        #infect people
        people_to_infect = init_infected
        while people_to_infect > 0:
            buffer = random.choice(self.people)
            if buffer.vaccinated == False:
                buffer.infected = True
                people_to_infect -= 1
        random.shuffle(self.people)

    def infected_people(self):
        #returns a list containing the indices of infect people objects
        infected_indices = []
        for i in range(len(self.people)):
            if self.people[i].infected == True and self.people[i].dead == False:
                infected_indices.append(i)
        return infected_indices

    def vaccinated_people(self):
        #returns a list containing the indices of infect people objects
        vaccinated_indices = []
        for i in range(len(self.people)):
            if self.people[i].vaccinated == True and self.people[i].dead == False:
                vaccinated_indices.append(i)
        return vaccinated_indices

    def normal_people(self):
        normal_indices = []
        for i in range(len(self.people)):
            if self.people[i].infected == False and self.people[i].vaccinated == False and self.people[i].dead == False:
                normal_indices.append(i)
        return normal_indices

    def dead_people(self):
        indices = []
        for i in range(len(self.people)):
            if self.people[i].dead:
                indices.append(i)
        return indices

    def step(self):
        # find all infected people
        infected_indices = self.infected_people()
        new_infections = []

        # calculate interactions
        saved = 0
        normal_people = self.normal_people()
        for i in infected_indices:
            for x in range(100):
                person = random.choice(self.people)
                if person.vaccinated == False:
                    if self.virus.rep_rate >= random.random():
                        new_infections.append(person)
                else:
                    saved += 1
                

        # calculate dead people
        for i in infected_indices:
            probability = random.random()
            if probability <= self.virus.mort_rate:
                self.people[i].vaccinated = True
            else:
                self.people[i].dead = True
            self.people[i].infected = False

        #infect new people
        for person in new_infections:
            person.infected = True

        ip = len(self.infected_people())
        self.logger.log(len(self.normal_people()), len(self.vaccinated_people()), ip, len(self.dead_people()), saved)
        if ip <= 0:
            self.logger.log_questions()

if __name__ == '__main__':
    if len(sys.argv) < 7:
        print("{population size} {vacc_percentage} {virus_name} {mortality_rate} {repro_rate} {optional: number of people initially infected}")
        quit()
    arg_list = sys.argv
    simulation = Simulation( int(arg_list[1]), float(arg_list[2]), str(arg_list[3]), float(arg_list[4]), float(arg_list[5]), int(arg_list[6]) )
    
    random.seed(time())
    print("Simulations STARTING")
    steps = 0
    while len(simulation.infected_people()) > 0:
        print("")
        simulation.step()
        steps += 1

    
    print(f"\nSteps: {steps}")