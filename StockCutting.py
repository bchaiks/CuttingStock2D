import json
from Solver.Solution import Solution

""" Cutting Stock Solver """

def StockCutting(inputData, sheetSize):
    partData = inputData.get_json()['dimensions']
    return(Solution(partData, sheetSize))

