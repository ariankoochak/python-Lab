from modules import *


# for windows
commodityPath = "c:\\Users\\Arian\\Desktop\\Code\python-Lab\\final-project\\data\\commodity.csv"
costumerPath = "c:\\Users\\Arian\\Desktop\\Code\python-Lab\\final-project\\data\\costumers.csv"
factorPath = "c:\\Users\\Arian\\Desktop\\Code\python-Lab\\final-project\\data\\factor.csv"

#for mac
# commodityPath = "/Users/arian.koochakgmail.com/Desktop/Code/python-Lab/final-project/data/commodity.csv"
# costumerPath = '/Users/arian.koochakgmail.com/Desktop/Code/python-Lab/final-project/data/costumers.csv'
# factorPath = '/Users/arian.koochakgmail.com/Desktop/Code/python-Lab/final-project/data/factor.csv'

commodities = cleanFile(readFile(commodityPath))
costumers = cleanFile(readFile(costumerPath))
factors = cleanFactorFile(readFile(factorPath),commodities)


def adminPanel(panelMode,idPointer = ''):
    clearTerminal()
    global commodities
    global costumers
    global factors
    match panelMode:
        case 'home':
            print('\nwelcome to admin panel \n\nProduct List(P)\nCostumers List(C)\nFactors List(F)\nAdd Factor(A)')
            command = getCommand('p','c','f','a')
            match command:
                case 'a':
                    adminPanel('addFactor')
                case 'f':
                    adminPanel('factorList')
                case 'c':
                    adminPanel('costumerList')
                case 'p':
                    adminPanel('productList')
                case _:
                    print('invalid command')
        case 'productList':
            showDatas(commodities)
            print('\n\nback(B)\t\tedit(E)\t\tremove(R)\t\taddProduct(A)')
            command = getCommand('b','e','r','a')
            match command:
                case 'a':
                    adminPanel('addProduct')
                case 'r':
                    adminPanel('removeProduct')
                case 'e':
                    adminPanel('editProduct')
                case 'b':
                    adminPanel('home')
                case _:
                    print('invalid command')
        case 'addProduct':
            product = getNewProduct(commodities)
            if(isinstance(product,bool)):
                if product:
                    adminPanel('editProduct',str(product))
                else:
                    adminPanel('productList')
            else:
                pushToFile(commodityPath,product)
                commodities = cleanFile(readFile(commodityPath))
                print('product added successfully!')
                input('press enter for continue... ')
                adminPanel('productList')
        case 'editProduct':
            if idPointer == '':
                showDatas(commodities)
                name = input(f'\n\nenter product name for change : ')
                for i in range(1,len(commodities.keys())):
                     if (commodities[str(i)]['name'] == name):
                        idPointer = str(i)
            clearTerminal()
            editedProduct = editData(commodities,idPointer,'product')
            editFile(commodityPath,editedProduct,idPointer)
            print('product edited successfully!')
            input('press enter for continue... ')
            commodities = cleanFile(readFile(commodityPath))
            adminPanel('productList')
        case 'removeProduct':
            if idPointer == '':
                showDatas(commodities)
                name = input(f'\n\nenter product name for delete : ')
                for i in range(1,len(commodities.keys())):
                     if (commodities[str(i)]['name'] == name):
                        idPointer = str(i)
            clearTerminal();
            command = input(f'Are you sure you want to delete {commodities[idPointer]["name"]}?(y/n) ')
            if command.lower() == 'y':
                deleteFromFile(commodityPath,idPointer)
                print('\n\nproduct removed successfully!')
                input('press enter for continue... ')
            commodities = cleanFile(readFile(commodityPath))
            adminPanel('productList')
        case 'costumerList':
            showDatas(costumers)
            print('\n\nback(B)\t\tedit(E)\t\tremove(R)\t\taddCostumers(A)')
            command = getCommand('b','e','r','a')
            match command:
                case 'a':
                    adminPanel('addCostumer')
                case 'r':
                    adminPanel('removeCostumer')
                case 'e':
                    adminPanel('editCostumer')
                case 'b':
                    adminPanel('home')
                case _:
                    print('invalid command')
        case 'addCostumer':
            costumer = getNewCostumer(costumers)
            pushToFile(costumerPath,costumer)
            costumers = cleanFile(readFile(costumerPath))
            print('costumer added successfully!')
            input('press enter for continue... ')
            adminPanel('costumerList')   
        case 'editCostumer':
            if idPointer == '':
                showDatas(costumers)
                idPointer = input(f'\n\nenter costumer id for change : ')
            clearTerminal()
            editedCostumer = editData(costumers,idPointer,'costumer')
            editFile(costumerPath,editedCostumer,idPointer)
            print('costumer edited successfully!')
            input('press enter for continue... ')
            costumers = cleanFile(readFile(costumerPath))
            adminPanel('costumerList')    
        case 'removeCostumer':
            if idPointer == '':
                showDatas(costumers)
                idPointer = input(f'\n\nenter costumer id for delete : ')
            command = input(f'Are you sure you want to delete {costumers[idPointer]["name"]} {costumers[idPointer]["family"]}?(y/n) ')
            if command.lower() == 'y':
                deleteFromFile(costumerPath,idPointer)
                print('\n\nproduct edited successfully!')
                input('press enter for continue... ')
            costumers = cleanFile(readFile(costumerPath))
            adminPanel('costumerList')
        case 'factorList':
            showDatas(factors,True)
            print('\n\nback(B)\t\tedit(E)\t\tremove(R)\t\taddFactor(A)')
            command = getCommand('b','e','r','a')
            match command:
                case 'a':
                    adminPanel('addFactor')
                case 'r':
                    adminPanel('removeFactor')
                case 'e':
                    adminPanel('editFactor')
                case 'b':
                    adminPanel('home')
                case _:
                    print('invalid command')
        case _:
            print('invalid panelMode')

adminPanel('home')
