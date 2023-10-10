"""
This code provides a simple implementation of each individual traffic light
in the PiTraffic Traffic Light shield.
"""
from gpiozero import *
from time import sleep

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

# basic on off commands
southRed.on()
sleep(2)
southRed.off()

"""
IDEAS
can create a class, where each object is a light that has properties: 
- color (red, green, yellow)
- direction (south, west, east, north)

however this all really, depending on the finite state machine design 
"""

