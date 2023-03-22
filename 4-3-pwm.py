import RPi.GPIO as GPIO

freq = 100
out_pin = 2

GPIO.setmode(GPIO.BCM)

GPIO.setup(out_pin, GPIO.OUT)

pwm = GPIO.PWM(out_pin, freq)

pwm.start(0)
try:
    while True:
        dt = float(input("Enter new duty cycle:"))
        pwm.ChangeDutyCycle(dt)
        evalue = (dt / 100) * 3.3
        print("Expected value:", evalue)
finally:
    pwm.stop()
    GPIO.output(out_pin, 0)
    GPIO.cleanup()