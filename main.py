from VacuumCleaner import *
from VacuumEnvironment import *

if __name__ == "__main__":
    agent = VacuumCleaner()
    environment = VacuumEnvironment4Path()
    environment.add_thing(agent)
    environment.run()
    print(environment.status)
    