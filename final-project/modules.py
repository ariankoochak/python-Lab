import os
import platform

commodityTitle = []
TerminalWidth = os.get_terminal_size().columns

def readFile(path):
    db = open(path,'r')
    exp = db.readlines();
    db.close();
    return exp

def cleanFile(inp):
    exp = {}
    inp[0] = inp[0][:-1].split(',')
    exp['titles'] = inp[0]
    for i in range(1,len(inp)):
        inp[i] = inp[i][:-1].split(',')
        preDict = {}
        for j in range(1,len(inp[i])):
            preDict[inp[0][j]] = inp[i][j]
        exp[inp[i][0]] = preDict 
    return exp

def showDatas(inp,isFactor = False):
    print("="*TerminalWidth)
    for key in inp:
        if key != 'titles':
            print()
            print(key," ",end="")
            for i in inp[key]:
                if isFactor:
                    temp = f'\t{inp[key][i]}'
                    if i == 'sum':
                        temp = f'\t\t{inp[key][i]}'
                    print(temp,end="")
                else:
                    print("%15s"%inp[key][i],end="")

def handleOrderInFactor(inp):
    inp = inp.split(';')
    for i in range(len(inp)):
        inp[i] = inp[i].split(':')
    return inp

def handleBooleanDataInFactor(inp):
    return (inp.upper() == 'TRUE')

def calculateSumInFactor(orders,commoditiesLits):
    exp = 0
    for item in orders:
        exp += int(commoditiesLits[item[0]]['price']) * int(item[1])
    return str(exp)

def pricePrettier(inp):
    exp = []
    saved = []
    for i in range(len(inp)-1,-1,-1):
        saved.append(inp[i])
        if len(saved) == 3:
            saved.reverse();
            exp.append(''.join(saved))
            saved.clear()
    if len(inp) % 3 != 0:
        saved.reverse();
        exp.append(''.join(saved))
    exp.reverse()
    return f"{'.'.join(exp)} Toman"

def handleVisualOrderInFactor(inp,commoditiesLits):
    for i in range(len(inp)):
        inp[i] = f'{commoditiesLits[inp[i][0]]["name"]} -> {inp[i][1]} adad'
    return inp

def cleanFactorFile(inp,commoditiesLits):
    exp = {}
    inp[0] = inp[0][:-1].split(',')
    exp['titles'] = inp[0]
    for i in range(1,len(inp)):
        inp[i] = inp[i][:-1].split(',')
        preDict = {}
        for j in range(1,len(inp[i])):
            if inp[0][j] == 'payment_sit' or inp[0][j] == 'is_sent':
                preDict[inp[0][j]] = handleBooleanDataInFactor(inp[i][j])
            elif inp[0][j] == 'orders':
                preDict[inp[0][j]] = handleOrderInFactor(inp[i][j])
            elif inp[0][j] == 'sum':
                if inp[i][j] == 'null':
                    preDict[inp[0][j]] = pricePrettier(calculateSumInFactor(preDict['orders'],commoditiesLits))
                else:
                    preDict[inp[0][j]] = inp[i][j]
            else:
                preDict[inp[0][j]] = inp[i][j]
        exp[inp[i][0]] = preDict
        exp[inp[i][0]]['orders'] = handleVisualOrderInFactor(exp[inp[i][0]]['orders'],commoditiesLits)
        # print(exp)
    return exp

def getCommand(*allowedCommands):
    exp = input('enter your command : ').lower()
    while exp not in allowedCommands:
        exp = input('\nenter valid command: ')
    return exp

def clearTerminal():
    deleteMod = 'clear'
    if platform.system() == 'Windows':
        deleteMod = 'cls'
    os.system(deleteMod)

def getNewProduct(inp):
    exp = []
    command = None
    newId = str(int(list(inp.keys())[-1])+1)
    for key in inp['titles']:
        if key == 'name':
            name = input(f'enter {key} : ')
            for i in list(inp.keys())[1:]:
                if (inp[i]['name'] == name):
                    command = input(f'your product is duplicate do you want to change it?(y/n): ')
                    if (command.lower() == 'y'):
                        return True
                    return False
            exp.append(name)
        elif key != 'id':
            exp.append(input(f'enter {key} : '))
        else:
            exp.append(newId)
    return ','.join(exp)

def getNewCostumer(inp):
    exp = []
    newId = str(int(list(inp.keys())[-1])+1)
    for key in list(inp.keys())[1:]:
        if key != 'id':
            exp.append(input(f'enter {key} : '))
        else:
            exp.append(newId)
    return ','.join(exp)

def editData(inp,id,mode):
    exp = []
    for key in inp['titles']:
        if key != 'id':
            temp = input(f'\nenter new {key} (default value = {inp[id][key]}): ')
            if key != 'name' and mode == 'product':
                while isInt(temp) == False:
                    temp = input(f'\nplease enter valid data (default value = {inp[id][key]}): ')
            exp.append(temp)
        else:
            exp.append(id)
    return ','.join(exp)

def editFactor(factors,id,costumers,commodities):
    exp = []
    productsForFactor = '';
    productsForCalculate = []
    temp = []
    for i in factors[id]['orders']:
        i = i.split(' -> ');
        i[0] = findProductIdFromName(commodities,i[0])
        i[1] = i[1].split(' ')[0]
        temp.append(':'.join(i))
        productsForCalculate.append(i)
    productsForFactor = ';'.join(temp)
    for key in factors['titles']:
        temp = id
        if key == 'costumer_id':
            showDatas(costumers);
            temp = input(f'\nenter new {key} (default value = {factors[id][key]}): ')
            while findFromId(costumers,temp) == -1:
                temp = input(f'\nplease enter valid data (default value = {factors[id][key]}): ')
        elif key == 'payment_sit' or key == 'is_sent':
            temp = input(f'\nenter new {key} (default value = {factors[id][key]}): ').upper()
            while not(temp == 'TRUE' or temp == 'FALSE'):
                temp = input(f'\nplease enter valid data (default value = {factors[id][key]}): ').upper()
        elif key == 'orders':
            showDatas(commodities)
            temp = input(f'\nenter new {key} (default value = {factors[id][key]}) (example value = product id ->2: numbers ->1;5:2;4:1;6:3): ')
            if(temp == ''):
                temp = productsForFactor;
                print(temp)
        elif key == 'sum':
            temp = pricePrettier(calculateSumInFactor(productsForCalculate,commodities))
        elif key != 'id':
            temp = input(f'\nenter new {key} (default value = {factors[id][key]}): ')
        exp.append(temp)
    return ','.join(exp)

def pushToFile(path,lineForAdd):
    db = open(path,'a')
    db.write(lineForAdd+'\n')
    db.close()

def editFile(path,lineForAdd,id):
    db = open(path,'r')
    exp = db.readlines()
    db.close()
    for i in range(len(exp)):
        temp = exp[i].split(',')
        if temp[0] == id:
            exp[i] = lineForAdd+'\n'
    db = open(path,'w')
    db.write(''.join(exp))
    db.close()

def deleteFromFile(path,id):
    db = open(path,'r')
    exp = db.readlines()
    db.close()
    for i in range(len(exp)):
        temp = exp[i].split(',')
        if temp[0] == id:
            exp.pop(i)
            break;
    db = open(path,'w')
    db.write(''.join(exp))
    db.close()
    
def isInt(inp):
    for i in inp:
        if(i < '0' or i > '9'):
            return False
    return True

def showFactorDetails(factors,costumers,id):
    print("==factor"+("="*(TerminalWidth-8)))
    costumerId = factors[id]["costumer_id"]
    
    for key in costumers[costumerId]:
        if(key != 'id'):
            print(f"\n\tcostumer {key}: {costumers[costumerId][key]}")
            
    print('\n\tpayment sit: ',end ="")
    if(factors[id]["payment_sit"]):
        print('payed!')
    else:
        print('pending for pay...')
        
    print("\n\torders:")
    for product in factors[id]["orders"]:
        print(f"\n\t\t{product}",end='')
        
    print(f"\n\n\torder sit: ",end="")
    if(factors[id]["is_sent"]):
        print('sent\n')
    else:
        print('pending for sent...\n')
    temp = f"====price of order : {factors[id]['sum']}"
    print(temp+("="*(TerminalWidth-len(temp))))
    
def findProductIdFromName(inp,name):
    for i in inp.keys():
        if i != 'titles':
            if inp[i]['name'] == name:
                return i
    return -1

def findFromId(inp,id):
    for i in inp.keys():
        if i == id:
            return inp[i]
    return -1

def getFactor(factors,costumers):
    pass