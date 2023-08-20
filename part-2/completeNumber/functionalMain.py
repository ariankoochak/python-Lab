def completeNumber(n):
    sum = 0
    for i in range(1,n//2+1):
        if n // i == n / i:
            sum += i
    if sum == n:
        return f'{n} is complete number'
    else:
        return f'{n} is not complete number'


n = int(input('enter your number : '))
print(completeNumber(n))