def isPrime(num):
    for i in range(2,num//2+1):
        if num // i == num / i:
            return False
    return True
inp = int(input('enter max : '))
one = None
two = None
counter = 0
for i in range(2,inp):
    realPrime = isPrime(i)
    if realPrime:
        if one == None:
            one = i
        else:
            two = i
    if one != None and two != None:
        if(abs(one - two) == 2):
            counter += 1
            print(f'[{one},{two}]')
        one = two
        two = None
print(counter)