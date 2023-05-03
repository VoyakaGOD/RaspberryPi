import RPi.GPIO as GPIO
from time import *
import matplotlib.pyplot as plt

T = 0.01

GPIO.setmode(GPIO.BCM)

dac = [26, 19, 13, 6, 5, 11, 9, 10]
GPIO.setup(dac, GPIO.OUT)

comp = 4
GPIO.setup(comp, GPIO.IN)

troyka = 17
GPIO.setup(troyka, GPIO.OUT, initial = GPIO.HIGH)

leds = [21, 20, 16, 12, 7, 8, 25, 24]
GPIO.setup(leds, GPIO.OUT)

def bin2dec(bin):
    dec = 0
    p = 1
    for bit in bin[::-1]:
        dec += p * int(bit)
        p *= 2
    return dec

def dec2bin(dec):
    return [int(bit) for bit in bin(dec)[2:].zfill(8)]

def adc():
    bits = [0, 0, 0, 0, 0, 0, 0, 0]
    for x in range(8):
        bits[x] = 1
        GPIO.output(dac, bits)
        sleep(0.001)
        if GPIO.input(comp) == 0:
            bits[x] = 0
    return bin2dec(bits)

def set_troyka_voltage(v):
    GPIO.output(troyka, v)

def set_leds(dec):
    GPIO.output(leds, dec2bin(dec))

try:
    GPIO.output(troyka, 1)
    while adc() > 0.01:
        continue
    times = []
    values = []
    GPIO.output(troyka, 0)
    while(1):
        sleep(T)
        x = adc()
        set_leds(x)
        volt = 3.3*x/256
        print(dec2bin(x), 'c->', volt)
        times += [time()]
        values += [volt]
        if volt > 3.15:
            break
    GPIO.output(troyka, 1)
    while(1):
        sleep(T)
        x = adc()
        set_leds(x)
        volt = 3.3*x/256
        print(dec2bin(x), 'd->', volt)
        times += [time()]
        values += [volt]
        if volt < 0.815:
            break

    freq = len(times) / (times[-1] - times[0])

    plt.plot(times, values)
    plt.show()
    print("full time:", times[-1] - times[0])
    print("T:", T + 0.001)
    print("freq:", freq)
    print("q:", 3.3 / 256)

    with open("data.txt", "w") as file:
        for value in values:
            file.write(str(value) + "\n")

    with open("settings.txt", "w") as file:
        file.write(str(freq) + "\n")
        file.write(str(3.3/256))

finally:
    GPIO.output(leds, 0)
    GPIO.cleanup()