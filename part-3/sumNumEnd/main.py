# sum = 0
# while True:
#     n = input("enter number(if end=> print end): ")
#     if n == 'end':
#         break;
#     else:
#         sum += int(n)
# print(sum)

sum = 0
isEnd = 'y'
while isEnd == 'y':
    sum += int(input("enter number: "))
    isEnd = input("aya adad degei ie dari?(y/n): ")
print(sum)