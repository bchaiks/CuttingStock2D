import json
from collections import OrderedDict

''' 
Set the inputs in the following two fields.
The output is returned (waaaaaay at the bottom)
as JSON object called Output -- go to the bottom 
to operate on the output however you need to. 
'''

# if this is TRUE it runs for the test dictionary 
# given at the end... set it to FALSE for production runs 
# (or I can just take this out...)

testing = True

#Input = ...
#SheetSize = ...

""" Stock Cutting Solver """

# Solver Objects #######################################

class Parameters:
	edgeMargin = 1.0
	partMargin = 1.0
	sheetMargin = 5.0
	def __init__(self, sheetSize):
		self.sheetSize = sheetSize

class SheetObject:
	def __init__(self, Parameters, indexNumber):  
		
		self.Index = indexNumber
		self.currentParts = []
		self.extremePoints = [[0,0,0]]
		
		self.fullSize = Parameters.sheetSize
		self.useableSize = [self.fullSize[0] - 2*Parameters.edgeMargin, 
							self.fullSize[1] - 2*Parameters.edgeMargin]
		
		self.yCoordinate = (Parameters.sheetMargin + self.fullSize[1]) * self.Index
		self.Coordinates = OrderedDict([('sheet', self.Index), ('x', 0), ('y', self.yCoordinate)])

class PartObject:
	def __init__(self, dimensions, label, positionInInputList):
		self.Dim = dimensions
		self.Area = self.Dim[0]*self.Dim[1]
		self.Label = label
		self.Index = positionInInputList
		self.SheetIndex = None
		self.Position = None
		self.ExtremePointIndex = None
	
	def FormatOutput(self, parameters):
		if self.SheetIndex is None:
			return("Can only run this AFTER placing the parts")	 
		margin = parameters.edgeMargin
		ySheetCoordinate = (parameters.sheetMargin + parameters.sheetSize[1]) * self.SheetIndex
		xPosition = self.Position[0] + margin
		yPosition = self.Position[1] + margin + ySheetCoordinate
		return(OrderedDict([('part', self.Label),('x', xPosition), ('y', yPosition)]))

##############################################################
# functions for formatting input #############################
def FormattedInput(inputPartDict):
	Labels = list(inputPartDict.keys())
	partObjects = []	
	for i in range(len(Labels)):
		Dims = inputPartDict[Labels[i]]
		partObjects.append(PartObject(Dims, Labels[i], i))
	return(partObjects)		
	
def FormattedOutput(reOrderedPartObjects, sheetObjects, parameters):
	
	originalOrderPartsList = sorted(reOrderedPartObjects, key=lambda part: part.Index)

	partOutput = [Part.FormatOutput(parameters) for Part in originalOrderPartsList]
	sheetOutput = [Sheet.Coordinates for Sheet in sheetObjects]
	
	partsAndSheets = OrderedDict([('parts',partOutput),('sheets',sheetOutput)])
	formattedOutput = OrderedDict([("results",partsAndSheets)])
	return(json.dumps(formattedOutput))

############################################################
# Geometry functions #######################################

def CheckFeasibility(newPart, candidatePositionIndex, sheet):
	candidatePosition = sheet.extremePoints[candidatePositionIndex]
	check = True	
	
	for i in range(2):		# check if violate sheet limits
		if newPart.Dim[i] + candidatePosition[i] > sheet.useableSize[i]:
			check = False	
	for j in range(len(sheet.currentParts)):	# check if overlap with current parts
		if overlap(newPart,candidatePosition, sheet.currentParts[j]): 
			check = False			
	return check


def overlap(Part1, position, Part2):
	ov = True
	
	if position[0] >= Part2.Dim[0] + Part2.Position[0]:
		ov = False
	if Part2.Position[0] >= position[0] + Part1.Dim[0]:
		ov = False
	if position[1] >= Part2.Dim[1] + Part2.Position[1]:
		ov = False
	if Part2.Position[1] >= position[1] + Part1.Dim[1]:
		ov = False	
	return ov
		
def TakesProjection(Part1, Part2, proj_dir):
	pd = proj_dir	
	od = 1-pd
	check = True

	if Part2.Dim[pd] + Part2.Position[pd] > Part1.Position[pd]:
		#i.e. piece is further from axis in projection direction 
		check = False
	if  Part2.Position[od] > Part1.Position[od]:
		#i.e. piece too far
		check = False
	if Part2.Position[od] + Part2.Dim[od] < Part1.Position[od] :
		# i.e. piece not far enough
		check = False
	return check

#########################################################
# Merit Function for Positioning ########################

def BoundingBox(newPart, candidatePositionIndex, sheet):	
	candidatePosition = sheet.extremePoints[candidatePositionIndex]
	X = candidatePosition[0] + newPart.Dim[0]
	Y =  candidatePosition[1] + newPart.Dim[1]
		
	for i in range(len(sheet.currentParts)):
		currentPart = sheet.currentParts[i]
		if currentPart.Position[0] + currentPart.Dim[0] > X:
			X = currentPart.Position[0] + currentPart.Dim[0]
		if currentPart.Position[1] + currentPart.Dim[1] > Y:
			Y = currentPart.Position[1] + currentPart.Dim[1]
	
	val = X*Y + X 	# Slightly penalizing things far in the X dimension	
	return(val)

#####################################################
# Sorting Functions #################################
def Randomize(partObjects):
	# eventually want to randomize the order and re-run the 
	# whole thing to get a broader picture of the solution space
	return(partObjects)

def SortArrayByArgMinIndex(array,index):
	''' MAKE SURE TO SORT BY MOST IMPORTANT INDEX LAST!!! '''
	a = array
	L = len(a)
	for i in range(L):
		temp = a[i]
		flag = 0
		j = 0
		while j < i and flag == 0:
			if temp[index] < a[j][index]:
				a[j+1] = a[j]
				a[j] = temp
				j += 1
			else:
				flag = 1
	return(a)

def UniqueValues(array):
	u_a = []
	L = len(array)
	for i in range(L):
		if array[i] in u_a:
			continue
		else:
			u_a.append(array[i])
	return(u_a)

########################################################
### Functions to add part to Sheet #####################
def NewExtremePoints(sheetObject, newPart, marginBetweenParts):
	''' lower left coordinate of newPart pushed out in x and y dimensions, 
	then projected onto the nearest part on the sheet (or the axis) '''
	p_m = marginBetweenParts
	D = newPart.Dim
	CI = sheetObject.currentParts
	CE = [Part.Position for Part in CI]
	EP = newPart.Position
	New_Eps = [[EP[0]+D[0] + p_m,EP[1]],
				[EP[0],EP[1]+D[1] + p_m]]

	Max_bounds = [-1., -1.]
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

def AddPartToSheet(sheetObject, newPart, marginBetweenParts):
	del sheetObject.extremePoints[newPart.ExtremePointIndex]
	for newExtremePoint in NewExtremePoints(sheetObject, newPart, marginBetweenParts):
		sheetObject.extremePoints.append(newExtremePoint)	
	for i in range(2):
		sheetObject.extremePoints = SortArrayByArgMinIndex(sheetObject.extremePoints,1-i)
	sheetObject.currentParts.append(newPart)

##################################################################
# Solve routine ##################################################

def FeasibleAndBestMerit(part, index, sheet, currentBest):
	if CheckFeasibility(part, index, sheet) and BoundingBox(part, index, sheet) < currentBest:
		return True
	else:
		return False 

def Solve(partList, sheetList, parameters):	
	for part in partList:
		bestMerit = 2 * parameters.sheetSize[0] * parameters.sheetSize[1]
		
		for i in range(len(sheetList)):
			sheet = sheetList[i] 
			for p in range(len(sheet.extremePoints)):
				if FeasibleAndBestMerit(part, p, sheet, bestMerit):
					bestMerit = BoundingBox(part, p, sheet)
					part.ExtremePointIndex = p
					part.SheetIndex = i
					part.Position = sheet.extremePoints[p]
		
		if part.SheetIndex is None:
			nextIndex = len(sheetList)
			sheetList.append(SheetObject(parameters, nextIndex))
			part.SheetIndex = len(sheetList) - 1
			part.ExtremePointIndex = 0
			part.Position = sheetList[part.SheetIndex].extremePoints[0]
			
		AddPartToSheet(sheetList[part.SheetIndex], part, parameters.partMargin)				

###############################################################
# Solution generator ##########################################

def Solution(rawPartDict, sheetSize, options = False):
	# options could signal the "randomized b&b" for instance...
	problemParameters = Parameters(sheetSize)
	Parts = []
	Sheets = []	
	unsortedPartObjects = FormattedInput(rawPartDict)
	
	if options:
		# do something else
		return("this functionality hasn't been configured yet.")
	else:
		Parts = sorted(unsortedPartObjects, key=lambda part: part.Area, reverse = True) 
		
	Solve(Parts, Sheets, problemParameters)
		
	return(FormattedOutput(Parts, Sheets, problemParameters))

############################################################################
# Call the solver and return a solution... #################################

def CutStock(inputData, sheetSize, Test = False):
    if Test:
        partData = OrderedDict(sorted(inputData.items(), key = lambda t: t[0]))
        return(Solution(partData, sheetSize))
    else:
        partData = inputData.get_json()['dimensions']
        partData = OrderedDict(sorted(partData.items(), key = lambda t: t[0]))
        return(Solution(partData, sheetSize))

if testing:
    test_dict = { '1': [45, 20], '2': [45, 20], '3': [45, 20],
				'4': [55, 25], '5': [35, 23] }
    sheet_size = [96.0, 48.0]
    test_Output = CutStock(test_dict, sheet_size, Test = testing)
    print(test_Output)

if not testing:
    Output = CutStock(Input, SheetSize)
    ## Do Something with the Output...
    print(Output)