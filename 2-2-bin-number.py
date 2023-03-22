import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

dac = [26, 19, 13, 6, 5, 11, 9, 10]
GPIO.setup(dac, GPIO.OUT)

number = [0, 0, 0, 0, 0, 0, 0, 0]

GPIO.output(dac, number)

sleep(10)

GPIO.output(dac, 0)
GPIO.cleanup()

#[255,  127,  64,   32,   5,    0,    256]
#[3.26, 1.63, 0.82, 0.45, 0.40, 0.32, 0.32]