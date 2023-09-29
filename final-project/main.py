from modules import *
import os

commodityPath = "c:\\Users\\Arian\\Desktop\\Code\python-Lab\\final-project\\data\\commodity.csv"

commodities = cleanFile(readFile(commodityPath))

showDatas(commodities)