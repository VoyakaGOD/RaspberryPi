import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

dac = [26, 19, 13, 6, 5, 11, 9, 10]
GPIO.setup(dac, GPIO.OUT)

comp = 4
GPIO.setup(comp, GPIO.IN)

troyka = 17
GPIO.setup(troyka, GPIO.OUT, initial = GPIO.HIGH)

leds = [21, 20, 16, 12, 7, 8, 25, 24]
GPIO.setup(leds, GPIO.OUT)

def dec2bin(dec):
    return [int(bit) for bit in bin(dec)[2:].zfill(8)]

def bin2dec(bin):
    dec = 0
    p = 1
    for bit in bin[::-1]:
        dec += p * int(bit)
        p *= 2
    return dec

def adc():
    bits = [0, 0, 0, 0, 0, 0, 0, 0]
    for x in range(8):
        bits[x] = 1
        GPIO.output(dac, bits)
        sleep(0.001)
        if GPIO.input(comp) == 0:
            bits[x] = 0
    return bin2dec(bits)

def get_progress_bar(dec):
    bits = [0, 0, 0, 0, 0, 0, 0, 0]
    for x in range(int((dec+4)/16), 8):
        bits[x] = 1
    return bits

try:
    while(1):
        x = adc()
        GPIO.output(leds, get_progress_bar(x))
        print(dec2bin(x), '->', 3.3*x/256)

finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()