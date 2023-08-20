def myPow(a,power):
    if power == 0:
        return 1
    multiply = a
    for i in range(1,power):
        multiply *= a

    return multiply


a = int(input('enter integer number : '))
power = int(input('enter pow : '))

if power < 0:
    print('enter mosbat pow')
else:
    print(f'{a}^{power} = {myPow(a,power)}')