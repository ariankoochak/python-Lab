from modules import *


commodityPath = r".\\data\\commodity.csv"
costumerPath = r".\\data\\costumers.csv"
factorPath = r".\\data\\factor.csv"

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
                name = input(f'\n\nenter product name for delete : ')
                if name == '--back':
                        adminPanel("productList")
                idPointer = findProductIdFromName(commodities,name)
                while idPointer == -1:
                    name = input(f'\n\nproduct not found,please try again : ')
                    if name == '--back':
                        adminPanel("productList")
                    idPointer = findProductIdFromName(commodities,name)
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
                if name == '--back':
                        adminPanel("productList")
                idPointer = findProductIdFromName(commodities,name)
                while idPointer == -1:
                    name = input(f'\n\nproduct not found,please try again : ')
                    if name == '--back':
                        adminPanel("productList")
                    idPointer = findProductIdFromName(commodities,name)
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
                if idPointer == '--back':
                        adminPanel("costumerList")
                while findFromId(costumers,idPointer) == -1:
                    idPointer = input(f'\n\nid not found,please try again : ')
                    if idPointer == '--back':
                        adminPanel("costumerList")
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
                if idPointer == '--back':
                        adminPanel("costumerList")
                while findFromId(costumers,idPointer) == -1:
                    idPointer = input(f'\n\nid not found,please try again : ')
                    if idPointer == '--back':
                        adminPanel("costumerList")
            command = input(f'Are you sure you want to delete {costumers[idPointer]["name"]} {costumers[idPointer]["family"]}?(y/n) ')
            if command.lower() == 'y':
                deleteFromFile(costumerPath,idPointer)
                print('\n\nproduct edited successfully!')
                input('press enter for continue... ')
            costumers = cleanFile(readFile(costumerPath))
            adminPanel('costumerList')
        case 'factorList':
            showDatas(factors,True)
            print('\n\nback(B)\t\tedit(E)\t\tremove(R)\t\taddFactor(A)\t\tshow Factor Details(S)')
            command = getCommand('b','e','r','a','s')
            match command:
                case 'a':
                    adminPanel('addFactor')
                case 'r':
                    adminPanel('removeFactor')
                case 'e':
                    adminPanel('editFactor')
                case 'b':
                    adminPanel('home')
                case 's':
                    adminPanel('showFactorDetails')
                case _:
                    print('invalid command')
        case 'showFactorDetails':
            if idPointer == '':
                showDatas(factors,True)
                idPointer = input(f'\n\nenter factor id for get details : ')
                if idPointer == '--back':
                        adminPanel("factorList")
                while findFromId(factors,idPointer) == -1:
                    idPointer = input(f'\n\nid not found,please try again : ')
                    if idPointer == '--back':
                        adminPanel("factorList")
            clearTerminal()
            showFactorDetails(factors,costumers,idPointer)
            print('\n\nback(B)\t\tedit(E)\t\tremove(R)')
            command = getCommand('b','e','r')
            match command:
                case 'r':
                    adminPanel('removeFactor',idPointer)
                case 'e':
                    adminPanel('editFactor',idPointer)
                case 'b':
                    adminPanel('factorList')
                case _:
                    print('invalid command')
        case "editFactor":
            if idPointer == '':
                showDatas(factors,True)
                idPointer = input(f'\n\nenter factor id for edit : ')
                if idPointer == '--back':
                        adminPanel("factorList")
                while findFromId(factors,idPointer) == -1:
                    idPointer = input(f'\n\nid not found,please try again : ')
                    if idPointer == '--back':
                        adminPanel("factorList")
            clearTerminal()
            editedFactor = editFactor(factors,idPointer,costumers,commodities)
            editFile(factorPath,editedFactor,idPointer)
            print('factor edited successfully!')
            input('press enter for continue... ')
            factors = cleanFactorFile(readFile(factorPath),commodities)
            adminPanel('factorList')
        case "removeFactor":
            if idPointer == '':
                showDatas(factors,True)
                idPointer = input(f'\n\nenter factor id for delete : ')
                if idPointer == '--back':
                        adminPanel("factorList")
                while findFromId(factors,idPointer) == -1:
                    idPointer = input(f'\n\nid not found,please try again : ')
                    if idPointer == '--back':
                        adminPanel("factorList")
            command = input(f'Are you sure you want to delete this factor?(y/n) ')
            if command.lower() == 'y':
                deleteFromFile(factorPath,idPointer)
                print('\n\nproduct edited successfully!')
                input('press enter for continue... ')
            factors = cleanFactorFile(readFile(factorPath),commodities)
            adminPanel('factorList')
        case "addFactor":
            newFactor = getFactor(factors,costumers,commodities)
            pushToFile(factorPath,newFactor)
            print('factor added successfully!')
            input('press enter for continue... ')
            adminPanel('factorList')   
        case _:
            print('invalid panelMode')
        
adminPanel('home')
