"""
Cutting Stock Solver
"""
import json
from Solver.Solution import Solution

def StockCutting(inputData):
    solverInput = inputData.get_json()['dimensions']
    return(Solution(solverInput))

