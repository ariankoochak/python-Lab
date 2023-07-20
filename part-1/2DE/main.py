import math

a = float(input('\tenter a : '))
if a == 0:
    print('\tERROR')
else:
    b = float(input('\tenter b : '))
    c = float(input('\tenter c : '))

    delta = (b**2)-(4 * a * c)

    if delta > 0:
        print('\twe have 2 roots:')
        x1 = ((-1 * b) + math.sqrt(delta))/(2 * a)
        x2 = ((-1 * b) - math.sqrt(delta))/(2 * a)
        print('\t\t',x1)
        print('\t\t',x2)
    elif delta == 0:
        print('\twe have 1 root:')
        x1 = (-1 * b)/(2 * a)
        if x1 == 0:
            x1 = '0.0'
        print('\t\t',x1)
    else:
        print('\t we dont have any roots')