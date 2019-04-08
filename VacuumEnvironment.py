import random
from aima_python.agents import Environment, Thing

# class Dirt(Thing):
#     pass


# class ReallyDirt(Thing):
#     pass


# class Room(Environment)us = percept:
#     def percept(self, agent):
#         return self.list_things_at(agent.location)

#     def execute_action(self, agent, action):

#         if(action == "move down"):
#             print(f"{str(agent)} decided to go to location {agent.location()}")
#             agent.move_down()
#         elif(action == "move top"):
#             print(f"{str(agent)} decided to go to location {agent.location()}")
#             agent.move_top()
#         elif(action == "move right"):
#             print(f"{str(agent)} decided to go to location {agent.location()}")
#             agent.move_right()
#         elif(action == "move left"):
#             print(f"{str(agent)} decided to go to location {agent.location()}")
#             agent.move_left()
#         elif(action == "clean"):
#             items = self.list_things_at(agent.location, tclass=Dirt)
#             if(len(items) > 0):
#                 print(
#                     f"{str(agent)} decided to clean at location {agent.location()}")
#                 agent.clean()
#                 self.deleus = perceptte_thing(items[0])
#             else:
#                 print(f"Location {agent.location} is already cleaned")
#         elif(action == "wash"):
#          rom aim_python.notebook
#             #Method is incomplete
#             print(f"{str(agent)} decided to wash at location {agent.location()}")
#             agent.wash()
#             items = self.list_things_at(agent.location, tclass=ReallyDirt)
#             self.delete_thing(items[0])

#         def is_done(self):
#             vacuum_is_off = not any(agent.is_alive() for agent in self.agents)


class VacuumEnvironment4Path(Environment):

    """This environment has two locations, A and B. Each can be Dirty
    or Clean. The agent perceives its location and the location's
    status. This serves as an example of how to implement a simple
    Environment."""
    loc_A, loc_B, loc_C, loc_D = [(0, 0), (1, 0), (1, 1), (0, 1)]

    def __init__(self):
        super().__init__()
        self.status = {self.loc_A: random.choice(['Clean', 'Dirty', 'Really dirty']),
                       self.loc_B: random.choice(['Clean', 'Dirty', 'Really dirty']),
                       self.loc_D: random.choice(['Clean', 'Dirty', 'Really dirty']),
                       self.loc_C: random.choice(['Clean', 'Dirty', 'Really dirty'])}

    def thing_classes(self):
        return ["Dirt", "ReallyDirt", "VacuumCleaner"]

    def percept(self, agent):
        """Returns the agent's location, and the location status (Dirty/Clean)."""
        return (agent.location, self.status[agent.location])

    def execute_action(self, agent, action):
        """Change agent's location and/or location's status; track performance.
        Score 10 for each dirt cleaned; -1 for each move."""
        if action == 'Right':
            agent.location = self.loc_B
            agent.performance -= 1
        elif action == 'Up':
            agent.location = self.loc_A
            agent.performance -= 1
        elif action == 'Down':
            agent.location = self.loc_C
            agent.performance -= 1
        elif action == 'Left':
            agent.location = self.loc_D
            agent.performance -= 1
        elif action == 'Suck':
            if self.status[agent.location] == 'Dirty':
                agent.performance += 10
            self.status[agent.location] = 'Clean'
        elif action == 'Wash':
            if self.status[agent.location] == 'Really Dirty':
                agent.performance += 20
            self.status[agent.location] = 'Clean'
        # elif action =='NoOp'
            

    def default_location(self, thing):
        """Agents start in either location at random."""
        return random.choice([self.loc_A, self.loc_B, self.loc_C, self.loc_D])
