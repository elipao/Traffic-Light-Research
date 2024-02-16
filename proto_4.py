import random 
from light_control_3 import * 
from time import sleep 

isEmergency = False 
TIMER = 0 

# how long does user want the program to run?  
user_timer = int(input("Simulation time (in seconds): "))

class State():
    # constructor 
    def __init__(self, ns_light, ew_light, delay_unit):
        self.ns_light = ns_light
        self.ew_light = ew_light
        self.delay_unit = delay_unit
        self.prev_state = None;   # keeps track if a state has been visited 2x
        self.prev_prev_state = None; 

    def get_input(self):
        ns_cars = random.randint(0, 7)
        ew_cars = random.randint(0, 7)
        # set of inputs = {11, 10, 01, 00}
        # NS | EW   
        #  1 | 1
        #  1 | 0 
        #  0 | 1
        #  0 | 0 

        # NS & EW TRAFFIC 
        if (ns_cars > 5) and (ew_cars > 5): # 11 
            return 3
        # NS TRAFFIC ONLY 
        elif (ns_cars > 5) and (ew_cars <= 5): # 10 
            return 2
        # EW TRAFFIC ONLY 
        elif (ew_cars > 5) and (ns_cars <= 5): # 01
            return 1
        # LOW OR NO TRAFFIC 
        else: # 00 
            return 0 
    
    def transition(self):
        global TIMER 
        # runs for length of user_timer input 
        while TIMER <= user_timer and not(isEmergency): 
            ns_lights_on(self.ns_light)
            ew_lights_on(self.ew_light)
            sleep(self.delay_unit)
            TIMER += self.delay_unit
            ns_lights_off(self.ns_light)
            ew_lights_off(self.ew_light)

            # save the prev_prev state and the prev_state 
            self.prev_prev_state = self.prev_state
            self.prev_state = self 

            # if in 2 consecutive states, force transition to next state 
            if ((self.prev_prev_state != None) and (self.prev_state != None)) and (self.prev_prev_state == self.prev_state):
                if self.prev_state == S0:
                    input = 0
                if self.prev_state == S2: 
                    input = 0 
            else:
                input = self.get_input() 

            # transition to next state 
            curr_state = state_table[self][input]
            curr_state.transition()

        if (isEmergency):
            emergency_lights()
            sleep(5)
            TIMER += 5 
            isEmergency = False 

        print("End of simulation\n")

# define each state (each state defined by ns and ew light color)
S0 = State("green", "red", 5)
S1 = State("yellow", "red", 1)
S2 = State("red", "green", 5)
S3 = State("red", "yellow", 1)
# states for the flashing green, indicating left turn signals 
S4 = State("flashing green", "red", 5)
S5 = State("red", "flashing green", 5)

# create hash table containing the transitions for each of the states (state table)
state_table = {
    S0: [S1, S1, S0, S0], 
    S1: [S2, S2, S2, S2], # no matter what, S1 goes to S2 
    S2: [S3, S2, S3, S2],
    S3: [S0, S0, S0, S0],  # no matter what, S3 goes to S0
}

S0.transition()