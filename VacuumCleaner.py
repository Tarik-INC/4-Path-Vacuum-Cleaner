# from aima_python.agents import Agent
# import Room

# class VacuumCleaner(Agent):
#     location = [0,0]

#     def move_up(self):
#         self.location[1] -= 1
#     def move_down(self):
#         self.location[1] += 1
#     def move_right(self):
#         self.location[0] += 1
#     def move_left(self):
#         self.location[0] = -1
#     def clean(self, thing):
#         print(f"Vacuum cleaner cleaned at {self.location} ")
#     def wash(self, thing):
#         print(f"Vacuum cleaner whased at {self.location}")

from VacuumEnvironment4Path import *
from aima_python.agents import *


# def program(self, percepts):
#         for p in percepts:
#             if isinstance(p, Dirt):
#                 return 'clean'
#             elif isinstance(p, ReallyDirt):
#                 return 'wash'
#         return


def ModelVacuumCleaner():
    """An model based vacuum cleaner agent that keeps track of what locations are 
    clean, dirty or really dirty.
    """
    loc_A = VacuumEnvironment4Path.loc_A
    loc_B = VacuumEnvironment4Path.loc_B
    loc_C = VacuumEnvironment4Path.loc_C
    loc_D = VacuumEnvironment4Path.loc_D

    model = {loc_A: None, loc_B: None, loc_C: None, loc_D: None}

    def program(percept):
        """Module responsible for taking a percept as input and return a defined action."""
        location, status = percept
        print(f"Vaccum cleaner at location {location}, it percepts status {status}")
        model[location] = status  # Update the model here
        if model[loc_A] == model[loc_B] == model[loc_C] == model[loc_D] == 'Clean':
            return 'NoOp'
        elif status == 'Dirty':
            return 'Suck'
        elif status == 'Really dirty':
            return 'Wash'
        elif location == loc_A:
            return 'Right'
        elif location == loc_B:
            return 'Down'
        elif location == loc_D:
            return 'Up'
        elif location == loc_C:
            return 'Left'
    return Agent(program)
