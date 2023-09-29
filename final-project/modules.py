import os
def readFile(path):
    db = open(path,'r')
    exp = db.readlines();
    db.close();
    return exp

def cleanFile(inp):
    exp = {}
    inp[0] = inp[0][:-1].split(',')
    for i in range(1,len(inp)):
        inp[i] = inp[i][:-1].split(',')
        preDict = {}
        for j in range(1,len(inp[i])):
            preDict[inp[0][j]] = inp[i][j]
        exp[inp[i][0]] = preDict 
    return exp

def showDatas(inp):
    TerminalWidth = os.get_terminal_size().columns
    print("="*TerminalWidth)
    counter = 1
    for key in inp:
        print()
        print(counter," ",end="")
        counter += 1
        for i in inp[key]:
            print("%15s"%inp[key][i],end="")