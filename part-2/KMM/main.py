def isPrime(inp):
    counter = int(inp/2)+1
    for i in range(2,counter):
        if inp // i == inp / i:
            return False
    return True


a = int(input('enter integer number : '))
b = int(input('enter integer number : '))

if a > b:
    smallNum = b
else:
    smallNum = a

inColumn = 1

if a <= 1 or b <= 1:
    print('please enter good number!')
else:
    while(not(isPrime(a)) and not(isPrime(b))):
        for i in range(2,smallNum):
            if (a // i == a / i) and (b // i == b / i):
                column = i
                inColumn *= i
                break
        a //= column
        b //= column
    print(f'KMM is => {inColumn*a*b}')