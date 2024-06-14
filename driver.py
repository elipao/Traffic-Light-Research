import random 
from light_control import * 
from time import sleep
from sound_control import *
from matrix_control import *

TIMER = 0
pwrButton = 4
buzzerPin = 18

GPIO.setmode(GPIO.BCM) 
GPIO.setup(pwrButton, GPIO.IN, pull_up_down=GPIO.PUD_UP)


# how long does user want the program to run?  
user_timer = int(input("Simulation time (in seconds greater than 10s): "))

class State():
    # constructor 
    def __init__(self, ns_light, ew_light, delay_unit):
        self.ns_light = ns_light
        self.ew_light = ew_light
        self.delay_unit = delay_unit
        self.prev_state = None;   # keeps track if a state has been visited 2x
        self.prev_prev_state = None; 

    def get_input(self):
        ns_cars = random.randint(0, 10)
        ew_cars = random.randint(0, 10)
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
        global button_pressed
        
 
        # runs for length of user_timer input 
        try: 
            while TIMER <= user_timer: 

                # pwrButton activates emergency vehicle situation
                if GPIO.input(pwrButton) == 0:
                    emergency_lights_on()
                    GPIO.output(buzzerPin, GPIO.HIGH)
                    sleep(6)
                    TIMER += 6
                    emergency_lights_off()
                    GPIO.output(buzzerPin, GPIO.LOW)
                else: 
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
                        input = 0; 
                    else:
                        input = self.get_input() 

                    # transition to next state 
                
                    curr_state = state_table[self][input]
                    curr_state.transition()
        except KeyboardInterrupt:
            GPIO.cleanup()

        print("End of simulation\n")

# define each state (each state defined by ns and ew light color)
S0 = State("green", "red", 5)
S1 = State("yellow", "red", 2)
S2 = State("red", "red", 1)
S3 = State("red", "flashing green", 5)
S4 = State("red", "flashing yellow", 3)
S5 = State("red", "red", 1)
S6 = State("red", "green", 5)
S7 = State("red", "yellow", 2)
S8 = State("red", "red", 1)
S9 = State("flashing green", "red", 5)
S10 = State("flashing yellow", "red", 3)
S11 = State("red", "red", 1)

# create hash table containing the transitions for each of the states (state table)
state_table = {
    S0: [S1, S1, S0, S0], 
    S1: [S2, S2, S2, S2], # no matter what, S1 goes to S2 
    S2: [S3, S3, S3, S3], # S2 always goes to S3... and so on
    S3: [S4, S3, S4, S3],  
    S4: [S5, S5, S5, S5],
    S5: [S6, S6, S6, S6], 
    S6: [S7, S6, S7, S6], 
    S7: [S8, S8, S8, S8], 
    S8: [S9, S9, S9, S9], 
    S9: [S10, S10, S9, S9], 
    S10: [S11, S11, S11, S11], 
    S11: [S0, S0, S0, S0] 
}


# matrix display Start message
main(cascaded=1, block_orientation=90, rotate=0, msg="Start")

# start the FSM at state 0(S0)  
S0.transition()

# matrix display End message
main(cascaded=1, block_orientation=90, rotate=0, msg="End")