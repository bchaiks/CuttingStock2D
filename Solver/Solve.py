from StockCutting.SolverObjects.SheetObject import SheetObject
import StockCutting.Solver.Geometry as gm
from ..SolverObjects.Processes.AddPartToSheet import AddPartToSheet 
from .MeritFunctions import BoundingBox

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
		
		if part.sheetIndex is None:
			nextIndex = len(sheetList)
			sheetList.append(SheetObject(parameters, nextIndex))
			part.sheetIndex = len(sheetList) - 1
			part.ExtremePointIndex = 0
			part.Position = sheet.extremePoints[0]
			
		AddPartToSheet(sheetList[part.sheetIndex], part, parameters.partMargin)				
					
def FeasibleAndBestMerit(part, index, sheet, currentBest):
	if gm.CheckFeasibility(part, index, sheet) and gm.BoundingBox(part, index, sheet) < currentBest:
		return True
	else:
		return False 