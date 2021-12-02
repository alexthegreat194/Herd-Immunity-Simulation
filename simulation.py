from _typeshed import Self
import random
import sys
from person import Person, State
from virus import Virus

class Simulation:
    def __init__(self, pop_size, vac_perc, virus_name, rep_rate, mort_rate, init_infected):
        #create virus
        self.virus = Virus(virus_name, rep_rate, mort_rate)
        
        #create people
        self.people = []
        for i in range(pop_size):
            self.people.append(Person())
        
        #give vaccines
        for i in range(int(pop_size * vac_perc)):
            self.people[i].state = State.VACCINATED
        random.shuffle(self.people)

        #infect people
        people_to_infect = init_infected
        while people_to_infect > 0:
            buffer = random.choice(self.people)
            if buffer.state == State.NORMAL:
                buffer.state == State.INFECTED
                people_to_infect -= 1
        random.shuffle(self.people)

    def step(self):

        '''
        MAKE A LIST OF PAST INFECTED PEOPLE AS A GLOBAL LIST !!!! AND AS KAROUND
        '''
        # find all infected people
        infected_indices = []
        for i in range(len(self.people)):
            if self.people[i].state == State.INFECTED:
                infected_indices.append(i)

        # calculate interactions
        for i in infected_indices:
            infected_person = self.people[i]
            for x in range(100):
                buffer = random.choice(self.people)
                probability = float(random.randrange(0, 100))/100
                if probability < self.virus.rep_rate:
                    if buffer.state == State.NORMAL:
                        buffer.state = State.INFECTED

        # RECALCULATE infected people
        infected_indices = []
        for i in range(len(self.people)):
            if self.people[i].state == State.INFECTED:
                infected_indices.append(i)

        # calculate dead people
        for i in infected_indices:
            buffer = self.people[i]
            probability = float(random.randrange(0, 100))/100
            if probability < self.virus.mort_rate:
                buffer.state = State.DEAD
            else:
                buffer.state = State.VACCINATED



if __name__ == '__main__':
    if len(sys.argv) < 7:
        print("{population size} {vacc_percentage} {virus_name} {mortality_rate} {repro_rate} {optional: number of people initially infected}")
        quit()
    arg_list = sys.argv
    simulation = Simulation( int(arg_list[1]), float(arg_list[2]), str(arg_list[3]), float(arg_list[4]), float(arg_list[5]), int(arg_list[6]) )