import threading
import os
import time
counter = 0
smallNumber = 0
def bmmCalc(a,b):
    global counter
    global smallNumber
    if a > b:
        biggerNum = a
        smallNum = b
    else:
        biggerNum = b
        smallNum = a

    bmm = -1
    smallNumber = int(smallNum)+1
    for i in range(smallNumber,0,-1):
        counter = i
        if (smallNum // i == smallNum / i) and (biggerNum // i == biggerNum / i):
            bmm = i
            break

    return bmm
n = 1

def mainThread():
    global n
    while(True):
        print(n)
        firstNumber = (n**17)+9
        secondNumber = ((n+1)**17)+9
        if bmmCalc(firstNumber,secondNumber) != 1:
            break
        n += 1
    print(n)

def loadThread():
    global counter
    global smallNumber
    global n
    while(counter > 0):
        percent = int(100 * (smallNumber - counter) / smallNumber)
        os.system('clear')
        print(f'{percent}%') 
        print('+'*percent,'-'*(100-percent),sep='')
        print(n)
        time.sleep(1)

main = threading.Thread(target=mainThread)
timer = threading.Thread(target = loadThread)

main.start()
timer.start()