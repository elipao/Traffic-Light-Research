from gpiozero import *

# SOUTH LED implementation
southRed = LED(17)   # where 17 corresponds to the GPIO 17 pin
southYellow = LED(27)
southGreen = LED(22)

# WEST LED implementation
westRed = LED(23)
westYellow = LED(24)
westGreen = LED(25)

# EAST LED implementation
eastRed = LED(16)
eastYellow = LED(20)
eastGreen = LED(21)

# NORTH LED implementation
northRed = LED(5)
northYellow = LED(6)
northGreen = LED(13)

# EMERGENCY LIGHTS, PULSE RED
def emergency_lights():
    northRed.pulse()
    eastRed.pulse()
    southRed.pulse()
    westRed.pulse() 

    southYellow.off()
    southGreen.off() 
    westYellow.off() 
    westGreen.off()
    eastYellow.off()
    eastGreen.off()
    northYellow.off()
    northGreen.off() 


# NS LIGHTS ON
def ns_lights_on(color):
    if color == "green": 
        northGreen.on()
        southGreen.on()
    elif color == "flashing green":
        northGreen.pulse()
        southGreen.pulse() 
    elif color == "yellow": 
        northYellow.on()
        southYellow.on() 
    else: 
        northRed.on()
        southRed.on() 
# NS LIGHTS OFF (clearing it out for the next transition)
def ns_lights_off(color):
    if color == "green": 
        northGreen.off()
        southGreen.off()
    elif color == "flashing green":
        northGreen.off()
        southGreen.off() 
    elif color == "yellow": 
        northYellow.off()
        southYellow.off() 
    else: 
        northRed.off()
        southRed.off() 
# EW LIGHTS ON
def ew_lights_on(color):
    if color == "green": 
        eastGreen.on()
        westGreen.on()
    elif color == "flashing green":
        eastGreen.pulse()
        westGreen.pulse() 
    elif color == "yellow": 
        eastYellow.on()
        westYellow.on() 
    else: 
        eastRed.on()
        westRed.on() 
# EW LIGHTS OFF
def ew_lights_off(color):
    if color == "green": 
        eastGreen.off()
        westGreen.off()
    elif color == "flashing green":
        eastGreen.off()
        westGreen.off() 
    elif color == "yellow": 
        eastYellow.off()
        westYellow.off() 
    else: 
        eastRed.off()
        westRed.off() 
    