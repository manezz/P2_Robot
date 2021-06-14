import re
import logging
from time import sleep
import threading
from serial_comm import SerialComm
import pimecha

robo = pimecha.PiMecha()
robo.connect("/dev/ttyUSB0")
#15 = 474    14 = 554
# id =   1   2   3   4   5   6   7   8   9  10  11  12  13  14  15  16  17
pos = [502,123,280,727,863,509,470,530,506,439,565,587,387,554,474,500,498]

for ID in range(17):
    robo.servoWrite(ID + 1, pos[ID], 500)
    sleep(0.05)

end = 16

def left():
    x = 1
    while(x <= end):
        x += 1
        sleep(0.55)
        if(x==2 or x==4):
            i = 2
            robo.servoWrite(i, pos[i-1]+300, 500)
            i = 10
            robo.servoWrite(i, pos[i-1]+100, 500)
        elif(x==3 or x==5):
            i = 2
            robo.servoWrite(i, pos[i-1]+100, 500)
            i = 10
            robo.servoWrite(i, pos[i-1]-100, 500)
        elif(x==6):
            i = 2
            robo.servoWrite(i, pos[i-1], 500)
            i = 10
            robo.servoWrite(i, pos[i-1]+100, 500)
        elif(x==7 or x==9):
            i = 3
            robo.servoWrite(i, pos[i-1]+520, 500)
            i = 10
            robo.servoWrite(i, pos[i-1]-100, 500)
        elif(x==8 or x==10):
            i = 3
            robo.servoWrite(i, pos[i-1], 500)
            i = 10
            robo.servoWrite(i, pos[i-1]+100, 500)
        else:
            i = 2
            robo.servoWrite(i, pos[i-1], 500)
            i = 10
            robo.servoWrite(i, pos[i-1], 500)


def right():
    x = 1
    y = 0
    while(y <= 6 and x <= end):
        x += 1
        sleep(0.55)
        if(x==2 or x==4):
            i = 5
            robo.servoWrite(i, pos[i-1]-300, 500)
            i = 11
            robo.servoWrite(i, pos[i-1]+100, 500)
        elif(x==3 or x==5):
            i = 5
            robo.servoWrite(i, pos[i-1]-100, 500)
            i = 11
            robo.servoWrite(i, pos[i-1]-100, 500)
        elif(x==6):
            i = 5
            robo.servoWrite(i, pos[i-1], 500)
            i = 11
            robo.servoWrite(i, pos[i-1]+100, 500)
        elif(x==7):
            i = 11
            robo.servoWrite(i, pos[i-1]-100, 500)
        elif(x==8 or x==10):
            i = 4
            robo.servoWrite(i, pos[i-1]-520, 500)
            i = 11
            robo.servoWrite(i, pos[i-1]+100, 500)
        elif(x==9 or x==11):
            i = 4
            robo.servoWrite(i, pos[i-1], 500)
            i = 11
            robo.servoWrite(i, pos[i-1]-100, 500)
        else:
            i = 5
            robo.servoWrite(i, pos[i-1], 500)
            i = 11
            robo.servoWrite(i, pos[i-1], 500)


def head():
    x = 1
    while(x <= end):
        x += 1
        sleep(0.55)
        if(x<=11 and x%2==0):
            i = 1
            robo.servoWrite(i, pos[i-1]-100, 500)
        elif(x<=11 and x>=3 and (x-3)%2==0):
            i = 1
            robo.servoWrite(i, pos[i-1]+100, 500)
        else:
            i = 1
            robo.servoWrite(i, pos[i-1], 500)


tl = threading.Thread(target=left)
tr = threading.Thread(target=right)
thead = threading.Thread(target=head)

def start():
    tl.start()
    tr.start()
    thead.start()

start()




