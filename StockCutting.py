"""
Cutting Stock Solver
"""
import json
# import SolutionObject

def StockCutting(inputData):
    parts = inputData.get_json()['dimensions']
    return Solution(parts).Output

