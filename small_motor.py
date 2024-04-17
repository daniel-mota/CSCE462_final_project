import RPi.GPIO as GPIO
import time

out4 = 40


GPIO.setmode(GPIO.BOARD)
GPIO.setup(out4,GPIO.OUT)


GPIO.output(out4,GPIO.HIGH)
try:
    while True:
        time.sleep(0.1)
except:

    GPIO.cleanup()