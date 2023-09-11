def bmmCalc(a,b):
    if a > b:
        biggerNum = a
        smallNum = b
    else:
        biggerNum = b
        smallNum = a

    bmm = -1

    for i in range(int(smallNum)+1,0,-1):
        if (smallNum // i == smallNum / i) and (biggerNum // i == biggerNum / i):
            bmm = i
            break

    return bmm



print()
n = 1
while(True):
    print(n)
    firstNumber = (n**17)+9
    secondNumber = ((n+1)**17)+9
    if bmmCalc(firstNumber,secondNumber) != 1:
        break
    n += 1

print(n)
