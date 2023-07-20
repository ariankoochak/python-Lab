inp = int(input('enter your number : '))
if inp > 0 and inp < 367:     
    dayPerMonth = 31
    plusToMonth = 1
    if inp >= 186:
        dayPerMonth = 30
        inp -= 186
        plusToMonth += 6

    day = inp % dayPerMonth
    month = int((inp - day)/dayPerMonth)+plusToMonth
    if day == 0:
        day = dayPerMonth
        month -= 1

    print(month,'/',day,sep='')
else :
    print('error')

