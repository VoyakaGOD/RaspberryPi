import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

leds = [21, 20, 16, 12, 7, 8, 25, 24]
GPIO.setup(leds, GPIO.OUT)

aux = [22, 23, 27, 18, 15, 14, 3, 2]
GPIO.setup(aux, GPIO.IN)

while True:
    for index in range(8):
        GPIO.output(leds[index], GPIO.input(aux[index]))
    if not GPIO.input(aux[0]) and not GPIO.input(aux[7]):
        break

GPIO.output(leds, 0)
GPIO.cleanup()