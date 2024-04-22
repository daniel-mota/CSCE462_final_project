import RPi.GPIO as GPIO
import time

button = 16

g = 25
f = 4
a = 19
b = 26

e = 13
d = 6
c = 5
button = 24
button2 = 23

GPIO.setmode(GPIO.BCM)
GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(button2, GPIO.IN, pull_up_down=GPIO.PUD_UP)


GPIO.setmode(GPIO.BCM)
# GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(a, GPIO.OUT)
GPIO.setup(b, GPIO.OUT)
GPIO.setup(c, GPIO.OUT)
GPIO.setup(d, GPIO.OUT)
GPIO.setup(e, GPIO.OUT)
GPIO.setup(f, GPIO.OUT)
GPIO.setup(g, GPIO.OUT)

GPIO.output(a, GPIO.HIGH)
GPIO.output(b, GPIO.HIGH)
GPIO.output(c, GPIO.HIGH)

cnt = 0

def display_number(num):
    segments = {
        0: [a, b, c, d, e, f],
        1: [b, c],
        2: [a, b, g, e, d],
        3: [a, b, c, d, g],
        4: [b, c, f, g],
        5: [a, c, d, f, g],
        6: [a, c, d, e, f, g],
        7: [a, b, c],
        8: [a, b, c, d, e, f, g],
        9: [a, b, c, d, f, g]
    }
    
    # Turn off all segments
    for segment in [a, b, c, d, e, f, g]:
        GPIO.output(segment, GPIO.LOW)
    
    # Turn on segments for the given number
    for segment in segments.get(num, []):
        GPIO.output(segment, GPIO.HIGH)

def button_callback(channel):
    global cnt
    cnt = ((cnt) % 9) + 1
    display_number(cnt)


def button_set(channel):
    global cnt
    global numPlayers
    global cardsPerPlayer
    display_number(0)
    if numPlayers == -1:
        numPlayers = cnt
        cnt = 0
        return
    cardsPerPlayer = cnt


try:
    display_number(0)
    GPIO.add_event_detect(button, GPIO.FALLING, callback=button_callback, bouncetime=200)
    GPIO.add_event_detect(button2, GPIO.FALLING, callback=button_set, bouncetime=200)

    numPlayers = -1
    cardsPerPlayer = -1

    while (numPlayers == -1 or cardsPerPlayer == -1):
        time.sleep(0.1)
    
    while True:
        time.sleep(0.3)
except:
    GPIO.cleanup()
