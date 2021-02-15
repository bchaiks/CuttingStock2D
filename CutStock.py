import json
from collections import OrderedDict
from Solver.Solution import Solution

""" Interface to Stock Cutting Solver """

def CutStock(inputData, sheetSize):
    #partData = inputData.get_json()['dimensions']
    #partData = OrderedDict(sorted(partData.items(), key = lamdbda t: t[0]))
    partData = OrderedDict(sorted(inputData.items(), key = lambda t: t[0]))
    return(Solution(partData, sheetSize))

