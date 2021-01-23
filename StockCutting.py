"""
Cutting Stock Solver
"""
import json
from Solver.Solution import Solution

def StockCutting(inputData, sheetSize):
	
    partData = inputData.get_json()['dimensions']
    
    return(Solution(partData, sheetSize))

