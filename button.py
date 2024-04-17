import RPi.GPIO as GPIO
import time

button = 21


GPIO.setmode(GPIO.BCM)
GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_UP)

cnt = 0
def button_callback():
    cnt += 1
    print("COUNT", cnt)

GPIO.add_event_detect(button, GPIO.FALLING, callback=button_callback, bouncetime=20000)