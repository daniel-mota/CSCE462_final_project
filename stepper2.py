import RPi.GPIO as GPIO
import time

out1 = 13
out2 = 11
out3 = 15
out4 = 12


GPIO.setmode(GPIO.BOARD)
GPIO.setup(out1,GPIO.OUT)
GPIO.setup(out2,GPIO.OUT)
GPIO.setup(out3,GPIO.OUT)
GPIO.setup(out4,GPIO.OUT)

GPIO.output(out1,GPIO.LOW)
GPIO.output(out2,GPIO.LOW)
GPIO.output(out3,GPIO.LOW)
GPIO.output(out4,GPIO.LOW)

players = int(input("How many players: "))
cardsPerPlayer = int(input("How many cards per player: "))

def shootCard():
    print("card shot")
    time.sleep(0.5)

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
    degrees = 360 / players
    # for i in range(cardsPerPlayer):
    rotateBase(-180)
    for i in range(players):
        rotateBase(degrees)
        for j in range(cardsPerPlayer):
            shootCard()
    rotateBase(-180)


shootCards(players, cardsPerPlayer)