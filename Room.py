from aima_python.agents import Environment, Thing

class Dirt(Thing):
    pass

class ReallyDirt(Thing):
    pass


class Room(Environment):
    def percept(self, agent):
        return self.list_things_at(agent.location)
    
    def execute_action(self, agent , action):

        if(action == "move down"):
            print(f"{str(agent)} decided to go to location {agent.location()}")
            agent.move_down()
        elif(action == "move top"):
            print(f"{str(agent)} decided to go to location {agent.location()}")
            agent.move_top()
        elif(action == "move right"):
            print(f"{str(agent)} decided to go to location {agent.location()}")
            agent.move_right()
        elif(action == "move left"):
            print(f"{str(agent)} decided to go to location {agent.location()}")
            agent.move_left()
        elif(action == "clean"):
            items = self.list_things_at(agent.location, tclass=Dirt)
            if(len(items) > 0):
                print(f"{str(agent)} decided to clean at location {agent.location()}")
                agent.clean()
                self.delete_thing(items[0])
            else:
                print(f"Location {agent.location} is already cleaned")
        elif(action == "wash"):
            #Method is incomplete
            print(f"{str(agent)} decided to wash at location {agent.location()}")
            agent.wash()
            items = self.list_things_at(agent.location, tclass=ReallyDirt)
            self.delete_thing(items[0])
            
        
        def is_done(self):
            vacuum_is_off = not any(agent.is_alive() for agent in self.agents)
        
    
