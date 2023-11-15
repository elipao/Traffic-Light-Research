# this file contains the logic for the finite state automata 
# contains the GUI for test purposes 
# (idea: have different Modes (auto, camera, random num generator (can set ranges)))
import random 
# import light_control
from time import sleep 

# If RUN = True, keep running program 
RUN = True 

# define the State class 
class State():
    def __init__(self, name, ns_light, ew_light, delay):
        self.name = name 
        self.ns_light = ns_light
        self.ew_light = ew_light
        self.delay = delay 

    # both (greater than 5 cars )= 11 (3 in decimal, decimal favored because it corresponds to index)
    # no traffic (both 0 cars) = 00 (0 in decimal)
    # ns traffic (ns greather than 5, ew less than or equal to 5) = 01 
    # ew traffic (ew greather than 5, ns less than or equal to 5) = 10 

    # irl it would just get the current camera car count, but since it's not installed, 
    # we will use a random number generator that goes from values 0 -> 7 
    # another option can be a simple auto mode where there's a loop iteration from input values 0->4 in which 
    # case there would be no variability or realistic value to demonstrate fsa 
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
        print("lights on\n")
        '''
        call functions from light_control, for now light_on is a placeholder function
        that can be later removed once running on a linux system 
        
        ns_light_on(self.ns_light)
        ew_light_on(self.ew_light)
        '''

    def light_off(self):
        print("lights off\n")
        '''
        ns_light_off(self.ns_light)
        ew_light_off(self.ew_light)
        '''

    def delay_time(self):
        print("delay\n")
        sleep(5)
    
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

    

    
