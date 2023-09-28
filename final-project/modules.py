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