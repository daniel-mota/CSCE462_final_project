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


# out1 = 13
# out2 = 11
# out3 = 15
# out4 = 12

out1 = 27
out2 = 17
out3 = 22
out4 = 18

motor1 = 21


# GPIO.setmode(GPIO.BOARD)
GPIO.setmode(GPIO.BCM)
GPIO.setup(out1,GPIO.OUT)
GPIO.setup(out2,GPIO.OUT)
GPIO.setup(out3,GPIO.OUT)
GPIO.setup(out4,GPIO.OUT)
GPIO.setup(motor1,GPIO.OUT)

GPIO.output(out1,GPIO.LOW)
GPIO.output(out2,GPIO.LOW)
GPIO.output(out3,GPIO.LOW)
GPIO.output(out4,GPIO.LOW)
GPIO.output(motor1,GPIO.LOW)



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

def turn_off_led():
    for segment in [a, b, c, d, e, f, g]:
        GPIO.output(segment, GPIO.LOW)

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


def shootCard(idx):
    shoot_time = [0.12, 0.1, 0.1, 0.1, 0.08, 0.08, 0.1, 0.08]
    GPIO.output(motor1,GPIO.HIGH)
    time.sleep(shoot_time[idx % len(shoot_time)])
    GPIO.output(motor1, GPIO.LOW)
    time.sleep(1.5)


def rotateBase(degree):
    x = int(degree / 360 * 408)
    output = [[1,0,0,0],
              [1,1,0,0],
              [0,1,0,0],
              [0,1,1,0],
              [0,0,1,0],
              [0,0,1,1],
              [0,0,0,1],
              [1,0,0,1]
            ]

    if x < 0:
        for i in range(-x, -1, -1):
            GPIO.output([out1, out2, out3, out4], output[i % 8])
            time.sleep(0.03)
    else:
        for i in range(x):
            GPIO.output([out1, out2, out3, out4], output[i % 8])
            time.sleep(0.03)
        
def shootCards(players, cardsPerPlayer):
    # print("hello")
    degrees = 360 / players
    # for i in range(cardsPerPlayer):
    rotateBase(-180)
    turn_off_led()
    for i in range(players):
        rotateBase(degrees)
        for j in range(cardsPerPlayer):
            shootCard(i * cardsPerPlayer + j)
            turn_off_led()
    rotateBase(-180)

try:
    display_number(0)
    GPIO.add_event_detect(button, GPIO.FALLING, callback=button_callback, bouncetime=300)
    GPIO.add_event_detect(button2, GPIO.FALLING, callback=button_set, bouncetime=300)

    numPlayers = -1
    cardsPerPlayer = -1
    while True:
        cnt = 0
        while (numPlayers == -1 or cardsPerPlayer == -1):
            time.sleep(0.1)
        turn_off_led()
        shootCards(numPlayers, cardsPerPlayer)
        display_number(0)
        numPlayers = -1
        cardsPerPlayer = -1
except:
    GPIO.cleanup()
