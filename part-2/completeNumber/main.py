n = int(input('enter your number :'))

sum = 0

for i in range(1,n):
    if n // i == n / i:
        sum += i

if sum == n:
    print(f'{n} is complete number')
else:
    print(f'{n} is not complete number')
