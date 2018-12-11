from sense_hat import SenseHat
import time
import random
import smtplib

sense = SenseHat()

sense.clear()

sense.show_message("Let's play!")

k=0
while k<3:
        
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


    def choose_symbolplayer1(r):
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

    def choose_symbolplayer2(r2):
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
    r = random.randint(1,5)
    r2 = random.randint(1,5)
    j=1
    while True and j<=2:
         x, y, z = sense.get_accelerometer_raw().values()

         x = abs(x)
         y = abs(y)
         z = abs(z)
         
         if x > 1.1 or y > 1.1 or z > 1.1:
             if j%2==1 :
                s=choose_symbolplayer1(r)
                time.sleep(1)
                sense.clear()
            
             elif j%2==0:
                ss=choose_symbolplayer2(r2)
                time.sleep(1)
                sense.clear()
             j=j+1

    equal = 0
    first = 0
    second = 0

    if r == r2:
        equal = equal + 1
    elif (r == 1) and ((r2 == 5) or (r2 == 4)):
        first = first + 1
    elif (r == 2) and ((r2 == 1) or (r2 == 5)):
        first = first + 1
    elif (r == 3) and ((r2 == 5) or (r2 == 2)):
        first = first + 1
    elif (r == 4) and (r2 == 3):
        first = first + 1
    elif (r == 5) and ((r2 == 4) or (r2 == 3)):
        first = first + 1
    else:
        second = second + 1
        
    
        
    k=k+1
if first > second:
    message = "1. player won"
elif first < second:
    message = "2. player won"
elif first==2 and equal==1:
    message = "1. player won"
elif second==2 and equal==1:
    message = "2. player won"
elif first ==1 and equal==2:
    message = "1. player won"
elif second ==1 and equal==2:
    message = "2. player won"
else:
    message = "Equal"
sense.show_message(message)

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("pythonteszteles@gmail.com", "Teszt123")
server.sendmail("pythonteszteles@gmail.com", "nikolettsos@gmail.com@gmail.com", message)
server.quit()