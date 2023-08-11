inp = input('enter your string: ')
upperCaseInp = ''
lowerCaseInp = ''
toggleCaseInp = ''
wordCaseInp = ''

for i in range(0,len(inp)):
    charCode = ord(inp[i])
    if charCode <= 122 and charCode >= 97:
        if i == 0 or ord(inp[i-1]) == 32:
            wordCaseInp += chr(charCode - 32)
        else:
            wordCaseInp += inp[i]
        upperCaseInp += chr(charCode - 32)
        toggleCaseInp += chr(charCode - 32)
        lowerCaseInp += inp[i]
    elif charCode <= 90 and charCode >= 65:
        lowerCaseInp += chr(charCode + 32)
        toggleCaseInp += chr(charCode + 32)
        upperCaseInp += inp[i]
        wordCaseInp += inp[i]
    else:
        upperCaseInp += inp[i]
        lowerCaseInp += inp[i]
        toggleCaseInp += inp[i]
        wordCaseInp += inp[i]

print(f'\nall upperCase:\n{upperCaseInp}')
print(f'\nall lowerCase:\n{lowerCaseInp}')
print(f'\ntoggleCase:\n{toggleCaseInp}')
print(f'\nwordcase:\n{wordCaseInp}')