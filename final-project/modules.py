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
def handleOrderInFactor(inp):
    inp = inp.split(';')
    for i in range(len(inp)):
        inp[i] = inp[i].split(':')
    return inp

def handlePaymentSitInFactor(inp):
    return (inp.upper() == 'TRUE')

def calculateSumInFactor(orders,inp,commoditiesLits):
    exp = 0
    for item in orders:
        exp += int(commoditiesLits[item[0]]['price']) * int(item[1])
    return exp

def cleanFactorFile(inp,commoditiesLits):
    exp = {}
    inp[0] = inp[0][:-1].split(',')
    for i in range(1,len(inp)):
        inp[i] = inp[i][:-1].split(',')
        preDict = {}
        for j in range(1,len(inp[i])):
            if inp[0][j] == 'payment_sit':
                preDict[inp[0][j]] = handlePaymentSitInFactor(inp[i][j])
            elif inp[0][j] == 'orders':
                preDict[inp[0][j]] = handleOrderInFactor(inp[i][j])
            elif inp[0][j] == 'sum':
                preDict[inp[0][j]] = calculateSumInFactor(preDict['orders'],inp[i][j],commoditiesLits)
            else:
                preDict[inp[0][j]] = inp[i][j]
        exp[inp[i][0]] = preDict
        # print(exp)
    return exp