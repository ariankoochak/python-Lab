number = ''
isInt = False
while not(isInt) or len(number) == 0:
    number = input('please enter number : ')
    for i in number:
        if ((i < '0' or i > '9') and i != ' ') and not(not(isInt) and (i == '-' or i == '+')):
            isInt = False
            break
        elif i >= '0' and i <= '9':
            isInt = True
number = number.replace(' ','')
print(f'your number is=> {number}')