from VacuumCleaner import *
from VacuumEnvironment4Path import *

if __name__ == "__main__":
    agent = ModelVacuumCleaner()
    environment = VacuumEnvironment4Path()
    environment.add_thing(agent)
    environment.run(steps=10)
    print('----------FINAL STATE----------')
    print(environment.status)
    