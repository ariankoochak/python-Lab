inp = input('enter your string: ')
upperCaseInp = ''
lowerCaseInp = ''
toggleCaseInp = ''
wordCaseInp = ''
# all capital
for i in range(0,len(inp)):
    charCode = ord(inp[i])
    if charCode <= 122 and charCode >= 97:
        upperCaseInp += chr(charCode - 32)
    else:
        upperCaseInp += inp[i]

print(f'\nall upperCase:\n{upperCaseInp}')

# all lower
for i in range(0,len(inp)):
    charCode = ord(inp[i])
    if charCode <= 90 and charCode >= 65:
        lowerCaseInp += chr(charCode + 32)
    else:
        lowerCaseInp += inp[i]

print(f'\nall lowerCase:\n{lowerCaseInp}')

# toggle
for i in range(0,len(inp)):
    charCode = ord(inp[i])
    if charCode <= 90 and charCode >= 65:
        toggleCaseInp += chr(charCode + 32)
    elif charCode <= 122 and charCode >= 97:
        toggleCaseInp += chr(charCode - 32)
    else:
        toggleCaseInp += inp[i]

print(f'\ntoggleCase:\n{toggleCaseInp}')

# word case
for i in range(0,len(inp)):
    charCode = ord(inp[i])
    if charCode <= 122 and charCode >= 97 and (i == 0 or ord(inp[i-1]) == 32):
        wordCaseInp += chr(charCode - 32)
    else:
        wordCaseInp += inp[i]

print(f'\nwordcase:\n{wordCaseInp}')