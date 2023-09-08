import os
import threading
import time

def isInt(inp):
    for i in inp:
        if i < '0' or i > '9':
            return False
    return True

def listMaker(inp):
    exp = inp.split(',')
    for i in range(len(exp)):
        exp[i] = exp[i].split(';')
        for j in range(len(exp[i])):
            k = exp[i][j]
            if k.upper() == 'YES' or k.upper() == 'NO':
                exp[i][j] = (k.upper() == 'YES')
            elif isInt(k):
                exp[i][j] = int(k)
            if len(exp[i]) == 1:
                exp[i] = exp[i][0]
    return exp

voteNum = []
sumNum = 0
def pushToVoteNum(name,num):
    global sumNum
    flag = True
    for vote in voteNum:
        if vote[0] == name:
            vote[1] += num
            flag = False
            break;
    if flag:
        voteNum.append([name,num])
    sumNum += num
def sortVote():
    global voteNum
    for i in range(0,len(voteNum)):
        for j in range(0,len(voteNum)):
            if(voteNum[i][1] > voteNum[j][1]):
                tmp = voteNum[i];
                voteNum[i] = voteNum[j];
                voteNum[j] = tmp;

f = open(r"c:\Users\Arian\Desktop\Code\python-Lab\part-7\readCSV\bigData.csv","r")
textFile = f.read().split('\n');
f.close();
counter = 0
def mainThread():
    global textFile
    global counter
    for i in range(1,len(textFile)):
        counter = i
        textFile[i] = listMaker(textFile[i])
        for j in range(0,len(textFile[i][2])):
            pushToVoteNum(textFile[i][2][j],textFile[i][3][j])
        counter = i
def loadThread():
    global textFile
    global voteNum
    global counter
    while(counter < len(textFile)-1):
        percent = int(100 * counter / len(textFile))
        os.system('cls')
        print(f'{percent}%') 
        print('+'*percent,'-'*(100-percent),sep='')
        time.sleep(0.25)
    print()
    sortVote()
    os.system('cls')
    print('100%\n','+'*100,sep='')
    for i in range(0,len(voteNum)):
        print(f"{voteNum[i][0]}=> {voteNum[i][1]}\t\t {int(voteNum[i][1] * 100 / sumNum)}%\n")

main = threading.Thread(target=mainThread)
timer = threading.Thread(target = loadThread)

main.start()
timer.start()






        
    


