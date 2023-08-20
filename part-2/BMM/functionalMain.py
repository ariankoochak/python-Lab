def bmmCalc(a,b):
    if a <= 0 or b <= 0:
        print('please enter + number')
    else:
        if a > b:
            biggerNum = a
            smallNum = b
        else:
            biggerNum = b
            smallNum = a

        bmm = -1

        for i in range(int(smallNum/2)+1,1,-1):
            if (smallNum // i == smallNum / i) and (biggerNum // i == biggerNum / i):
                bmm = i
                break

        if bmm == -1:
            return 'we dont have BMM'
        else:
            return f'BMM is {bmm}'

a = int(input('enter first number : '))
b = int(input('enter first number : '))

print(bmmCalc(a,b))

