from modules import *
import os

# commodityPath = "c:\\Users\\Arian\\Desktop\\Code\python-Lab\\final-project\\data\\commodity.csv" for windows
commodityPath = "/Users/arian.koochakgmail.com/Desktop/Code/python-Lab/final-project/data/commodity.csv"
costumerPath = '/Users/arian.koochakgmail.com/Desktop/Code/python-Lab/final-project/data/costumers.csv'
factorPath = '/Users/arian.koochakgmail.com/Desktop/Code/python-Lab/final-project/data/factor.csv'

commodities = cleanFile(readFile(commodityPath))
costumers = cleanFile(readFile(costumerPath))
factors = cleanFactorFile(readFile(factorPath),commodities)
showDatas(factors)