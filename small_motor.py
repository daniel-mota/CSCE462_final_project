import RPi.GPIO as GPIO
import time

motor1 = 21

GPIO.setmode(GPIO.BCM)
GPIO.setup(motor1,GPIO.OUT)

def shoot_card(t):
    GPIO.output(motor1,GPIO.HIGH)
    time.sleep(t)
    GPIO.output(motor1, GPIO.LOW)


try:
    time.sleep(0.5)
    shoot_card(0.12)
    time.sleep(1)
    shoot_card(0.12)
    time.sleep(1)
    shoot_card(0.1)
    time.sleep(1)
    shoot_card(0.1)
except:

    GPIO.cleanup()