import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

dac = [26, 19, 13, 6, 5, 11, 9, 10]
GPIO.setup(dac, GPIO.OUT)

def dec2bin(dec):
    return [int(bit) for bit in bin(dec)[2:].zfill(8)]

try:
    inp = input("Enter T:")
    T = 5
    dec = 0
    try:
        T = float(inp)
    finally:
        pass
    while True:
        while dec < 255:
            sleep(T/2/256)
            dec += 1
            GPIO.output(dac, dec2bin(dec))
        while dec > 0:
            sleep(T/2/256)
            dec -= 1
            GPIO.output(dac, dec2bin(dec))


finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()