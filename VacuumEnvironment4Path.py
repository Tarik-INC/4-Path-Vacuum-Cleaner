import random
from aima_python.agents import Environment, Thing


class VacuumEnvironment4Path(Environment):

    """This environment has four locations,A (0,0), B (0, 1), C (1, 1), D (1, 0). Each can be Dirty,
    Really Dirty or Clean and the registered agent perceives its location and the location's
    status."""
    loc_A, loc_B, loc_C, loc_D = [(0, 0), (1, 0), (1, 1), (0, 1)]

    def __init__(self):
        super().__init__()
        self.status = {self.loc_A: random.choice(['Clean', 'Dirty', 'Really dirty']),
                       self.loc_B: random.choice(['Clean', 'Dirty', 'Really dirty']),
                       self.loc_D: random.choice(['Clean', 'Dirty', 'Really dirty']),
                       self.loc_C: random.choice(['Clean', 'Dirty', 'Really dirty'])}
        print(f"Starting environment with Locations:\nA={self.loc_A},\nB={self.loc_B},\nC={self.loc_C},\nD={self.loc_D} ")

    def thing_classes(self):
        return ["Dirt", "ReallyDirt", "VacuumCleaner"]

    def percept(self, agent):
        """Returns the agent's location, and the location status (Dirty/Really dirty/Clean)."""
        return (agent.location, self.status[agent.location])

    def execute_action(self, agent, action):
        """Change agent's location and/or location's status; track performance.
        Score 10 for each dirt cleaned, 20 for each dirty washed; -1 for each move."""
        if action == 'Right':
            agent.location = self.loc_B
            agent.performance -= 1
            print('Vaccum cleaner is going right to B')
        elif action == 'Up':
            agent.location = self.loc_A
            agent.performance -= 1
            print('Vaccum cleaner is going up to A')
        elif action == 'Down':
            agent.location = self.loc_C
            agent.performance -= 1
            print('Vaccum cleaner is going down to C')
        elif action == 'Left':
            agent.location = self.loc_D
            agent.performance -= 1
            print('Vaccum cleaner is going left to D')
        elif action == 'Suck':
            if self.status[agent.location] == 'Dirty':
                agent.performance += 10
            print('Vaccum cleaner is sucking the dirty')
            self.status[agent.location] = 'Clean'
        elif action == 'Wash':
            if self.status[agent.location] == 'Really Dirty':
                agent.performance += 20
            print('Vacuum cleaner is washing the dirty')
            self.status[agent.location] = 'Clean'
        # elif action =='NoOp'
            

    def default_location(self, thing):
        """Agents start in either location at random."""
        return random.choice([self.loc_A, self.loc_B, self.loc_C, self.loc_D])
