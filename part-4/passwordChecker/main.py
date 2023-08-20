password = input('enter your password : ')

isNum = False
isUpperCase = False
isLowerCase = False
isChar = False
isNumToChar = False

for i in range(0,len(password)):
        myChar = password[i]
        if myChar <= '9' and myChar >= '0':
            isNum = True
        elif myChar >= 'A' and myChar <= 'Z':
            isUpperCase = True
        elif myChar >= 'a' and myChar <= 'z':
            isLowerCase = True
        elif myChar == '@' or myChar == '#' or myChar == '$' or myChar == '&' or myChar == '%':
            isChar = True
            if (i != 0 and password[i-1] <= '9' and password[i-1] >= '0') or (i+1 != len(password) and password[i+1] <= '9' and password[i+1] >= '0'):
                isNumToChar = True

errorTemplate = ''
if not(isNum):
    errorTemplate += 'your pass dont have Number \n'
if not(isUpperCase):
    errorTemplate += 'your pass dont have upper case character \n'
if not(isLowerCase):
    errorTemplate += 'your pass dont have lower case character \n'
if not(isChar):
    errorTemplate += 'your pass dont have characher \n'
if isNumToChar:
    errorTemplate += 'your number & character kenar ham \n'

if errorTemplate == '':
    print('your pass is verryyyy good')
else :
    print(errorTemplate)