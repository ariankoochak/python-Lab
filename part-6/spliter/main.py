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
print('\n\n')
print(listMaker('2015,134,NDP;Liberal;Green;CPC,4;1;2;3,YES;NO;YES') )
print('\n\n')
