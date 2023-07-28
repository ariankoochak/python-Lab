a = int(input('enter integer number : '))
b = int(input('enter integer number : '))

max = int(a > b) * a + int(a < b) * b
min = int(a < b) * a + int(a > b) * b

print(f'{max} > {min}')