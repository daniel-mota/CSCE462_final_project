import RPi.GPIO as GPIO
import time

button = 23


GPIO.setmode(GPIO.BCM)
GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_UP)

cnt = 0
def button_callback(channel):
    global cnt
    cnt += 1
    print("COUNT", cnt)

GPIO.add_event_detect(button, GPIO.FALLING, callback=button_callback, bouncetime=500)

try:
    while True:
        time.sleep(0.1)
except:
    GPIO.cleanup()
    
    