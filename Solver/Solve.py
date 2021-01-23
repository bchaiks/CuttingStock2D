from Solver.Geometry import *
from SolverObjects.Processes.AddPartToSheet import AddPartToSheet 
from Solver.MeritFunctions import BoundingBox

""" Solve function and ancillary... """

def Solve(partList, sheetList, sheetSize):
	
	for part in partList:
		
		candidatePosition = None
		bestMerit = 2 * sheetSize[0] * sheetSize[1]
		
		for i in range len(sheetList):
			sheet = sheetList[i] 
			for p in range(len(sheet.extremePoints)):
				if FeasibleAndBestMerit(part, p, sheet, bestMerit):
					bestMerit = BoundingBox(part, p, sheet)
					candidatePosition = p
					part.sheetIndex = i
		
		if part.sheetIndex is None:
			sheetList.append(SheetObject(sheetSize))
			part.sheetIndex = len(sheetList) - 1
			candidatePosition = 0
		
		AddPartToSheet(sheetList[part.sheetIndex], part)
					
					
def FeasibleAndBestMerit(part, index, sheet, currentBest):
	if CheckFeasibility(part, index, sheet) and BoundingBox(part, index, sheet) < currentBest:
		return True
	else:
		return False 