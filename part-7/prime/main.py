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

inp = int(input('enter number : '))
counter = 0
for i in range(1,inp):
    if bmmCalc(i,inp) == 1:
        counter += 1
        print(i)
print(counter)