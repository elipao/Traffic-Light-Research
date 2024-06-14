import RPi.GPIO as GPIO
import time 

buzzer_pin = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(buzzer_pin, GPIO.OUT)

def sound_buzzer():
    GPIO.output(buzzer_pin, GPIO.HIGH)
    time.sleep(3)
    GPIO.output(buzzer_pin, GPIO.LOW)
    GPIO.cleanup() 