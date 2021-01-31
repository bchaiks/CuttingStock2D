#import json
from Solver.Solution import Solution

""" Interface to Stock Cutting Solver """

def CutStock(inputData, sheetSize):
    #partData = inputData.get_json()['dimensions']
    partData = inputData
    return(Solution(partData, sheetSize))

