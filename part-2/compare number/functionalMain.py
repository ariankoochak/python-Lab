def compareNum(a,b):
    max = int(a > b) * a + int(a < b) * b
    min = int(a < b) * a + int(a > b) * b


    if max == min:
        return f'{max} = {min}'
    else:
        return f'{max} > {min}'


a = int(input('enter integer number : '))
b = int(input('enter integer number : '))

print(compareNum(a,b))