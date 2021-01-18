"""
Cutting Stock Solver
"""
import json
from Solver.Solution import Solution

def StockCutting(inputData):
    parts = inputData.get_json()['dimensions']
    return(Solution(parts).Output)

