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
	
	def UpdateExtremePoints(self):
		# updates current list of extreme points based on 
		# self.currentParts...
		# so whenever add a part, to Sheets[i], then do 
		# Sheets[i].UpdateExtremePoints()
		
		