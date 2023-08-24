sentence = input("enter your sentence : ")
for i in range(0,len(sentence)):
    if not(sentence[i] in sentence[0 : i]):
        iCounter = 0
        for j in range(i,len(sentence)):
            if sentence[j] == sentence[i]:
                iCounter += 1
        print(f'{sentence[i]} => {iCounter}\n')