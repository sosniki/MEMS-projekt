from sense_hat import SenseHat
import time
import random

sense = SenseHat()

sense.clear()

sense.show_message("Let's play!")


f = [  0, 0, 0]
p = [255, 0, 0]
b = [0, 0, 255]


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
        sense.set_pixels(spock)
    elif r == 3:
        sense.set_pixels(paper)
    elif r == 4:
        sense.set_pixels(lizard)
    elif r == 5:
        sense.set_pixels(scissors)

        
stone2 = [
f,f,f,f,f,f,f,f,
f,f,p,p,p,p,f,f,
f,p,p,p,p,p,p,f,
p,p,p,p,p,p,p,p,
p,p,p,p,p,p,p,p,
f,p,p,p,p,p,p,f,
f,f,p,p,p,p,f,f,
f,f,f,f,f,f,f,f,
]

paper2 = [
f,f,f,f,f,f,f,f,
f,p,p,p,p,p,p,f,
f,p,p,p,p,p,p,f,
f,p,p,p,p,p,p,f,
f,p,p,p,p,p,p,f,
f,p,p,p,p,p,p,f,
f,p,p,p,p,p,p,f,
f,f,f,f,f,f,f,f,
]

scissors2 = [
p,p,f,f,f,f,p,p,
f,p,p,f,f,p,p,f,
f,f,p,p,p,p,f,f,
f,f,f,p,p,f,f,f,
p,p,p,p,p,p,p,p,
p,f,f,p,p,f,f,p,
p,f,f,p,p,f,f,p,
p,p,p,p,p,p,p,p,
]

lizard2 = [
f,f,f,f,f,f,f,f,
f,f,f,f,f,f,f,f,
f,p,p,p,p,p,p,f,
p,f,f,f,f,f,f,f,
p,f,f,f,f,f,f,f,
f,p,p,p,p,p,p,f,
f,f,f,f,f,f,f,f,
f,f,f,f,f,f,f,f,
]

spock2 = [
p,p,f,f,f,f,p,p,
f,p,p,f,f,p,p,f,
f,f,p,p,p,p,f,f,
p,p,p,p,p,p,p,p,
p,p,p,p,p,p,p,p,
f,p,p,p,p,p,p,f,
f,f,p,p,p,p,f,f,
f,f,p,p,p,p,f,f,
]

def choose_symbolplayer2():
    r2 = random.randint(1,5)
    if r2 == 1:
        sense.set_pixels(stone2)
    elif r2 == 2:
        sense.set_pixels(spock2)
    elif r2 == 3:
        sense.set_pixels(paper2)
    elif r2 == 4:
        sense.set_pixels(lizard2)
    elif r2 == 5:
        sense.set_pixels(scissors2)


for i in range (2):
     x, y, z = sense.get_accelerometer_raw().values()

     x = abs(x)
     y = abs(y)
     z = abs(z)
     
    if i==0 and (x > 1.1 or y > 1.1 or z > 1.1):

        choose_symbolplayer1()
        time.sleep(1)
        sense.clear()
        
    elif i==1 and (x > 1.1 or y > 1.1 or z > 1.1):
        choose_symbolplayer2()
        time.sleep(1)
        sense.clear()
      
    if r % 5 == r2:
       sense.show_message("Second player wins!")
    elif (r + 1) % 5 == r2:
       sense.show_message("Second player wins!")
    elif r == r2:
       sense.show_message("Players tie!")
    else:
       sense.show_message("First player wins!")
    
