from Processes.Sorting import *
from Solver.Geometry import TakesProjection

""" adding a new part to a sheet """

def AddPartToSheet(sheetObject, newPart):
	
	del sheetObject.extremePoints[newPart.ExtremePointIndex]
	
	for newExtremePoint in NewExtremePoints(sheetObject,newPart):
		sheetObject.extremePoints.append(newExtremePoint)
		
	for i in range(2):
		sheetObject.extremePoints = SortArrayByArgMinIndex(sheetObject.extremePoints,1-i)
	
	sheetObject.currentParts.append(newPart)
	

def NewExtremePoints(sheetObject, newPart):
	'''
	lower left coordinate of newPart pushed out in x and y dimensions, 
	then projected onto the nearest part on the sheet (or the axis)
	'''
	p_m = sheetObject.marginBetweenParts
	D = newPart.Dim
	CI = sheetObject.currentParts
	CE = [Part.LowerLeftCoordinate for Part in CI]
	EP = newPart.LowerLeftCoordinate
	New_Eps = [[EP[0]+D[0] + p_m,EP[1]],
				[EP[0],EP[1]+D[1] + p_m]]

	Max_bounds = [-1., -1. ]

	for i in range(len(CI)):
		# shrinking y coordinate
		if TakesProjection(newPart, CI[i],1) and CE[i][1] + CI[i].Dim[1] + p_m > Max_bounds[1]:
			New_Eps[0] = [EP[0] + D[0] + p_m, CE[i][1] + CI[i].Dim[1] + p_m]
			Max_bounds[0] = CE[i][1] + CI[i].Dim[1] + p_m
		
		# shrinking x coordinate
		if TakesProjection(newPart, CI[i],0) and CE[i][0] + CI[i].Dim[0] + p_m > Max_bounds[0]:
			New_Eps[1] = [CE[i][0] + CI[i].Dim[0] + p_m, EP[1] + D[1] + p_m]
			Max_bounds[1] = CE[i][0] + CI[i].Dim[0] + p_m	

	return (UniqueValues(New_Eps))
