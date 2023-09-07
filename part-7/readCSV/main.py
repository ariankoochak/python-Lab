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
def pushToVoteNum(name,num):
    flag = True
    for vote in voteNum:
        if vote[0] == name:
            vote[1] += num
            flag = False
            break;
    if flag:
        voteNum.append([name,num])

f = open("/Users/arian.koochakgmail.com/Desktop/Code/python-Lab/part-7/readCSV/info.csv","r")
textFile = f.read().split('\n');
f.close();


for i in range(1,len(textFile)):
    textFile[i] = listMaker(textFile[i])
    for j in range(0,len(textFile[i][2])):
        pushToVoteNum(textFile[i][2][j],textFile[i][3][j])

print()
for i in range(0,len(voteNum)):
    print(f"{voteNum[i][0]} => {voteNum[i][1]}\n")
