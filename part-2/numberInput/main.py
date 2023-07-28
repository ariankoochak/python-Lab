count = 0

while count != 20 and count != 50 and count != 100:
    count = int(input('please enter 20 or 50 or 100 : '))

small = float(input('enter number : '))
big = float(input('enter number : '))
s = small + big

if small > big:
    ch = small
    small = big
    big = ch

for i in range(2,count):
    inp = float(input('enter number : '))
    s += inp
    if small > inp:
        small = inp
    if big < inp:
        big = inp

print(f'\nsmallest number => {small}\nbiggest number => {big}\naverage => {s/count}\nsum => {s}')