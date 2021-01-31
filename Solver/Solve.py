from .SolverObjects.SheetObject import SheetObject
from .Processes.Geometry import *
from .AddPartToSheet import AddPartToSheet 
from .Processes.MeritFunctions import BoundingBox

""" Solve function and ancillary... """

def Solve(partList, sheetList, parameters):	
	for part in partList:
		bestMerit = 2 * parameters.sheetSize[0] * parameters.sheetSize[1]
		
		for i in range(len(sheetList)):
			sheet = sheetList[i] 
			for p in range(len(sheet.extremePoints)):
				if FeasibleAndBestMerit(part, p, sheet, bestMerit):
					bestMerit = BoundingBox(part, p, sheet)
					part.ExtremePointIndex = p
					part.sheetIndex = i
					part.Position = sheet.extremePoints[p]
		
		if part.SheetIndex is None:
			nextIndex = len(sheetList)
			sheetList.append(SheetObject(parameters, nextIndex))
			part.SheetIndex = len(sheetList) - 1
			part.ExtremePointIndex = 0
			part.Position = sheetList[part.SheetIndex].extremePoints[0]
			
		AddPartToSheet(sheetList[part.SheetIndex], part, parameters.partMargin)				
					
def FeasibleAndBestMerit(part, index, sheet, currentBest):
	if CheckFeasibility(part, index, sheet) and BoundingBox(part, index, sheet) < currentBest:
		return True
	else:
		return False 