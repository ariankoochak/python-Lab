a = int(input('enter integer number : '))
power = int(input('enter pow : '))



if power < 0:
    print('enter mosbat pow')
else:
    if power == 0:
        multiply = 1
    else:
        multiply = a

    for i in range(1,power):
        multiply *= a

    print(f'{a}^{power} = {multiply}')