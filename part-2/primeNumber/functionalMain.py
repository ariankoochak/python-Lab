import math

def isPrime(inp):
    if inp <= 0 or inp%2 == 0:
        return False
    else:
        counter = int(inp/2)+1
        for i in range(3,int(math.sqrt(counter))+1,2):
            if inp // i == inp / i:
                return False
    return True


inp = int(input('enter integer number: '))
if isPrime(inp):
    print('Your Number is Prime')
else:
    print('Your Number is not Prime')

