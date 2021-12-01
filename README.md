# Herd-Immunity-Simulation

### Rules

1. A sick person only has a chance at infecting uninfected, unvaccinated people they encounter.  
1. An infected person cannot infect a vaccinated person. This still counts as an interaction.  
1. An infected person cannot infect someone that is already infected.  This still counts as an interaction.
1. At the end of a time step, an infected person will either die of the infection or get better.  The chance they will die is the percentage chance stored in `mortality_rate`.  
1. For simplicity's sake, if the person does not die, we will consider them immune to the virus and change `is_vaccinated` to `True` when this happens.  
1. Dead people can no longer be infected, either. Any time an individual dies, we should also change their `infected` attribute to `False`.  
1. All state changes for a person should occur at the **end** of a time step, after all infected persons have finished all of their interactions.  
1. During the interactions, make note of any new individuals infected on this step. After the interactions are over, we will change the `infected` attribute of all newly infected individuals to `True`.  
1. Resolve the states of all individuals that started the turn infected by determining if they die or survive the infection, and change the appropriate attributes.  
1. The simulation should output a logfile that contains a record of every interaction that occurred during the simulation.  We will use this logfile to determine final statistics and answer questions about the simulation.


## Basic Structure

The program consists of 4 classes: `Person`, `Virus`, `Simulation`, and `Logger`.

* `Simulation`: Highest level of abstraction. The main class that runs the entire simulation.
* `Person`: Represents the people that make up the population that the virus is spreading through.
* `Virus`: Models the properties of the virus we wish to simulate.
* `Logger`: A helper class for logging all events that happen in the simulation.