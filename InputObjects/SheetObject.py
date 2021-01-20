"""
Sheet Object

Stores:
- index
- part margin
- sheet margin - SAME FOR ALL SHEETS
- Position -- function of index 
- sheet size
- list of current Parts positioned on the sheet
"""
from Solver.Sorting import UniqueValues


class SheetObject:
	# i.e. ALL sheets share these
	marginAtSheetEdge = 1.0
	marginBetweenParts = 1.0
	marginBetweenSheets = 5.0
	
	# sheetSize given as input, so CAN CHANGE depending on problem
	def __init__(self, sheetSize):  
		
		# given when instantiated 
		self.index = None
		
		# array of PartObjects
		self.currentParts = []
		
		# open points where a Part can be positioned
		self.extremePoints = []
		
		self.fullSize = sheetSize
		self.usableSize = [fullSize[0] - 2*marginAtSheetEdge, fullSize[1] - 2*marginAtSheetEdge]
		
		#dictionary formatted position information
		self.yCoordinate = (5.0 + self.fullSize[1]) * self.index
		self.Coordinates = {'sheet': self.index, 'x': 0, 'y': self.yCoordinate}
	
	def UpdateExtremePoints(self, newPart):
		# updates current list of extreme points based on 
		# self.currentParts...
		# so whenever add a part, to Sheets[i], then do 
		# Sheets[i].UpdateExtremePoints(newPart)
		
		# newPart is a PartObject that has Dims and EP already, and 
		# the SheetObject (self) has the rest of it...
	def Update_EP(Dims, EP, Curr_EPs, Curr_Items, piece_margin):
	'''
	Dims = 1x2 WxD of current piece placed 
		(in orienation OR* decided by Feas and Merit...)
	EP = 1x2 coordinates of lower left corner of current piece
	Curr_EPs = list of current extreme points where Curr_Items
		are located 
	Curr_Items = list of dimensions of current items 

	idea is you take current EP and push it out in the 
	two dimensions of the current piece, then project
	each of these towards the other axes, ending up 
	on the closest current piece it "runs into"

	'''
	p_m = piece_margin
	D = Dims
	CI = Curr_Items
	CE = Curr_EPs
	New_Eps = [[EP[0]+D[0] + p_m,EP[1]],
				[EP[0],EP[1]+D[1] + p_m]]

	Max_bounds = [-1., -1. ]

	for i in range(len(CI)):
		# shrinking y coordinate
		if proj(D, EP, CI[i], CE[i],1) and CE[i][1] + CI[i][1] + p_m > Max_bounds[1]:
			New_Eps[0] = [EP[0] + D[0] + p_m, CE[i][1] + CI[i][1] + p_m]
			Max_bounds[0] = CE[i][1] + CI[i][1] + p_m
		

		# shrinking x coordinate
		if proj(D, EP, CI[i], CE[i],0) and CE[i][0] + CI[i][0] + p_m > Max_bounds[0]:
			New_Eps[1] = [CE[i][0] + CI[i][0] + p_m, EP[1] + D[1] + p_m]
			Max_bounds[1] = CE[i][0] + CI[i][0] + p_m	
		
	# remove duplicates
	#New_Eps = unq(New_Eps)
	return (UniqueValues(New_Eps))

		
		