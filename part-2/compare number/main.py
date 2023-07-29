a = int(input('enter integer number : '))
b = int(input('enter integer number : '))

max = int(a > b) * a + int(a < b) * b
min = int(a < b) * a + int(a > b) * b


if max == min:
    print(f'{max} = {min}')
else:
    print(f'{max} > {min}')