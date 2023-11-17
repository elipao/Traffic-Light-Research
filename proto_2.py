import random 
from light_control_2 import * 
from time import sleep 

RUN = True 

class State():
    def __init__(self, name, ns_light, ew_light, delay_unit):
        self.name = name 
        self.ns_light = ns_light
        self.ew_light = ew_light
        self.delay_unit = delay_unit

    def get_input(self):
        ns_cars = random.randint(0, 7)
        ew_cars = random.randint(0, 7)
        if (ns_cars > 5) and (ew_cars > 5):
            return 3 
        elif (ew_cars > 5) and (ns_cars <= 5):
            return 2
        elif (ns_cars > 5) and (ew_cars <= 5):
            return 1
        else:
            return 0 
    
    def light_on(self):
        ns_lights_on(self.ns_light)
        ew_lights_on(self.ew_light)

    def light_off(self):
        ns_lights_off(self.ns_light)
        ew_lights_off(self.ew_light)
  
    def delay_time(self):
        print("delay\n")
        sleep(self.delay_unit)
    
    def transition(self):
        if RUN: 
            print("transition\n")
            self.light_on()
            self.delay_time()
            self.light_off() 
            input = self.get_input() 
            print("input: " + str(input) + "\n")
            curr_state = state_table[self][input]
            print("Current state: " + curr_state.name + "\n")
            curr_state.transition()

        else:
            print("End of simulation\n")


# define each state   
S0 = State("state 0", "green", "red", 5)
S1 = State("state 1", "yellow", "red", 1)
S2 = State("state 2", "red", "green", 5)
S3 = State("state 3", "red", "yellow", 1)

# create hash table containing the transitions for each of the states 
state_table = {
    S0: [S0, S0, S1, S1], 
    S1: [S2, S2, S2, S2], 
    S2: [S3, S3, S2, S3],
    S3: [S0, S0, S0, S0] 
}

S0.transition()

    

    
