import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

dac = [26, 19, 13, 6, 5, 11, 9, 10]
GPIO.setup(dac, GPIO.OUT)

comp = 4
GPIO.setup(comp, GPIO.IN)

troyka = 17
GPIO.setup(troyka, GPIO.OUT, initial = GPIO.HIGH)

def dec2bin(dec):
    return [int(bit) for bit in bin(dec)[2:].zfill(8)]

def adc():
    for x in range(256):
        GPIO.output(dac, dec2bin(x))
        sleep(0.001)
        if GPIO.input(comp) == 0:
            return x
    return 0

try:
    while(1):
        x = adc()
        print(dec2bin(x), '->', 3.3*x/256)
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()