inp = int(input('enter integer number: '))
isPrime = True

if inp <= 0:
    isPrime = False
else:
    counter = int(inp/2)+1
    for i in range(2,counter):
        if inp // i == inp / i:
            isPrime = False
            break

if isPrime:
    print('Your Number is Prime')
else:
    print('Your Number is not Prime')