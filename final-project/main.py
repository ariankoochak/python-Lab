from modules import *
import os

TerminalWidth = os.get_terminal_size().columns

commodityPath = '/Users/arian.koochakgmail.com/Desktop/Code/python-Lab/final-project/data/commodity.csv'

commodities = cleanFile(readFile(commodityPath))




