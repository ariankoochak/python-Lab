x = int(input('enter x : '))
y = int(input('enter y : '))

s = "Niavaran";

if x < 0 or y < 0:
    print('enter true number')
else:
    if x > y:
        x,y = y,x
    for i in range(x,min(y,len(s))):
        print(s[i],end="")

print('\n')