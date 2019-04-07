from Room import *

def program(self, percepts):
        for p in percepts:
            if isinstance(p, Dirt):
                return 'clean'
            elif isinstance(p, ReallyDirt):
                return 'wash'
        return
