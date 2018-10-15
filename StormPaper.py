from sense_hat import SenseHat
import time
import random

sense = SenseHat()

sense.clear()

sense.show_message("Let's play!")


f = [  0, 0, 0]
b = [255, 0, 0]


stone = [
f,f,f,f,f,f,f,f,
f,f,b,b,b,b,f,f,
f,b,b,b,b,b,b,f,
b,b,b,b,b,b,b,b,
b,b,b,b,b,b,b,b,
f,b,b,b,b,b,b,f,
f,f,b,b,b,b,f,f,
f,f,f,f,f,f,f,f,
]

paper = [
f,f,f,f,f,f,f,f,
f,b,b,b,b,b,b,f,
f,b,b,b,b,b,b,f,
f,b,b,b,b,b,b,f,
f,b,b,b,b,b,b,f,
f,b,b,b,b,b,b,f,
f,b,b,b,b,b,b,f,
f,f,f,f,f,f,f,f,
]

scissors = [
b,b,f,f,f,f,b,b,
f,b,b,f,f,b,b,f,
f,f,b,b,b,b,f,f,
f,f,f,b,b,f,f,f,
b,b,b,b,b,b,b,b,
b,f,f,b,b,f,f,b,
b,f,f,b,b,f,f,b,
b,b,b,b,b,b,b,b,
]

lizard = [
f,f,f,f,f,f,f,f,
f,f,f,f,f,f,f,f,
f,b,b,b,b,b,b,f,
b,f,f,f,f,f,f,f,
b,f,f,f,f,f,f,f,
f,b,b,b,b,b,b,f,
f,f,f,f,f,f,f,f,
f,f,f,f,f,f,f,f,
]

spock = [
b,b,f,f,f,f,b,b,
f,b,b,f,f,b,b,f,
f,f,b,b,b,b,f,f,
b,b,b,b,b,b,b,b,
b,b,b,b,b,b,b,b,
f,b,b,b,b,b,b,f,
f,f,b,b,b,b,f,f,
f,f,b,b,b,b,f,f,
]


def choose_symbolplayer1():
    r = random.randint(1,5)
    if r == 1:
        sense.set_pixels(stone)
    elif r == 2:
        sense.set_pixels(paper)
    elif r == 3:
        sense.set_pixels(scissors)
    elif r == 4:
        sense.set_pixels(lizard)
    elif r == 5:
        sense.set_pixels(spock)

        
stone2 = [
f,f,f,f,f,f,f,f,
f,f,p,b,b,b,f,f,
f,b,b,b,b,b,b,f,
b,b,b,b,b,b,b,b,
b,b,b,b,b,b,b,b,
f,b,b,b,b,b,b,f,
f,f,b,b,b,b,f,f,
f,f,f,f,f,f,f,f,
]

paper2 = [
f,f,f,f,f,f,f,f,
f,p,b,b,b,b,b,f,
f,b,b,b,b,b,b,f,
f,b,b,b,b,b,b,f,
f,b,b,b,b,b,b,f,
f,b,b,b,b,b,b,f,
f,b,b,b,b,b,b,f,
f,f,f,f,f,f,f,f,
]

scissors2 = [
p,b,f,f,f,f,b,b,
f,b,b,f,f,b,b,f,
f,f,b,b,b,b,f,f,
f,f,f,b,b,f,f,f,
b,b,b,b,b,b,b,b,
b,f,f,b,b,f,f,b,
b,f,f,b,b,f,f,b,
b,b,b,b,b,b,b,b,
]

lizard2 = [
f,f,f,f,f,f,f,f,
f,f,f,f,f,f,f,f,
f,b,b,b,b,b,b,f,
b,f,f,f,f,f,f,f,
b,f,f,f,f,f,f,f,
f,b,b,b,b,b,b,f,
f,f,f,f,f,f,f,f,
f,f,f,f,f,f,f,f,
]

spock2 = [
p,b,f,f,f,f,b,b,
f,b,b,f,f,b,b,f,
f,f,b,b,b,b,f,f,
b,b,b,b,b,b,b,b,
b,b,b,b,b,b,b,b,
f,b,b,b,b,b,b,f,
f,f,b,b,b,b,f,f,
f,f,b,b,b,b,f,f,
]

def choose_symbolplayer2():
    r2 = random.randint(1,5)
    if r2 == 1:
        sense.set_pixels(stone2)
    elif r2 == 2:
        sense.set_pixels(paper2)
    elif r2 == 3:
        sense.set_pixels(scissors2)
    elif r2 == 4:
        sense.set_pixels(lizard2)
    elif r2 == 5:
        sense.set_pixels(spock2)


while True:
    x, y, z = sense.get_accelerometer_raw().values()

    x = abs(x)
    y = abs(y)
    z = abs(z)

    if x > 1.1 or y > 1.1 or z > 1.1:
        choose_symbolplayer1()
        time.sleep(1)
        sense.clear
        choose_symbolplayer2()
        time.sleep(1)
        sense.clear()
