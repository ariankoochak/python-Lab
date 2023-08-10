import math

inp = int(input('enter integer number: '))
isPrime = True

if inp <= 0 or inp%2 == 0:
    isPrime = False
else:
    counter = int(inp/2)+1
    for i in range(3,int(math.sqrt(counter))+1,2):
        if inp // i == inp / i:
            isPrime = False
            break

if isPrime:
    print('Your Number is Prime')
else:
    print('Your Number is not Prime')