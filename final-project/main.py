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


def adminPanel(panelMode,productIdForEdit = None):
    clearTerminal()
    global commodities
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
            product = getProduct(commodities)
            if(isinstance(product,int)):
                adminPanel('editProduct',product)
            else:
                pushToFile(commodityPath,product)
                commodities = cleanFile(readFile(commodityPath))
                print('product added successfully!')
                input('press enter for continue... ')
                adminPanel('productList')
        case 'editProduct':
            print(productIdForEdit)
        case _:
            print('invalid panelMode')

adminPanel('home')
