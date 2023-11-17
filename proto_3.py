import random 
from light_control_2 import * 
from time import sleep 

# RUN = True 
TIMER = 0 

# how long does user want the program to run?  
user_timer = int(input("Simulation time (in seconds): "))

class State():
    def __init__(self, ns_light, ew_light, delay_unit):
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
    
    def transition(self):
        global TIMER 
        if TIMER <= user_timer: # runs until a minute 
            ns_lights_on(self.ns_light)
            ew_lights_on(self.ew_light)
            sleep(self.delay_unit)
            TIMER += self.delay_unit
            ns_lights_off(self.ns_light)
            ew_lights_off(self.ew_light)
            input = self.get_input() 
            curr_state = state_table[self][input]
            curr_state.transition()
        else:
            print("End of simulation\n")

# define each state 
S0 = State("green", "red", 5)
S1 = State("yellow", "red", 1)
S2 = State("red", "green", 5)
S3 = State("red", "yellow", 1)

# create hash table containing the transitions for each of the states 
state_table = {
    S0: [S0, S0, S1, S1], 
    S1: [S2, S2, S2, S2], 
    S2: [S3, S3, S2, S3],
    S3: [S0, S0, S0, S0] 
}

S0.transition()