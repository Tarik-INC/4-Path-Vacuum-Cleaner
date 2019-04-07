from aima_python.agents import Agent
import Room

class VacuumCleaner(Agent): 
    location = [0,0]

    def move_up(self):
        self.location[1] -= 1
    def move_down(self):
        self.location[1] += 1
    def move_right(self):
        self.location[0] += 1
    def move_left(self):
        self.location[0] -= 1
    def clean(self, thing):
        print(f"Vacuum cleaner cleaned at {self.location} ")
    def wash(self, thing):
        print(f"Vacuum cleaner whased at {self.location}")
    

