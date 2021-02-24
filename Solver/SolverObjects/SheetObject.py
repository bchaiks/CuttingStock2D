
from collections import OrderedDict

""" Sheet Object """

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
	
	
		