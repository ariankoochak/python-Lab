arr = list()
a = 1
while a != 0:
    a = int(input("enter number : "))
    if a != 0:
        addIndex = 0
        for i in range(len(arr)):
            if arr[i] < a:
                addIndex = i + 1
        arr.insert(addIndex,a)
print(arr)
    
