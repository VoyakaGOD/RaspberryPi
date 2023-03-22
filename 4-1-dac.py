import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

dac = [26, 19, 13, 6, 5, 11, 9, 10]
GPIO.setup(dac, GPIO.OUT)

def dec2bin(dec):
    return [int(bit) for bit in bin(dec)[2:].zfill(8)]


try:
    while True:
        inp = input("Enter[0-255]:")
        if inp == 'q':
            break
        if not inp.isdigit():
            print("You should enter only digits, DIGITS!!!")
            continue
        bin_val = dec2bin(int(inp))
        if len(bin_val) > 8:
            print("Number is to long for 8 bits!!!")
            continue
        GPIO.output(dac, bin_val)
        dac_value = int(inp)/256 * 3.3
        print("DAC:", dac_value, "V")
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()