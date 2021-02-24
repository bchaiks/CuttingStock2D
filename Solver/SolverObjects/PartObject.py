from collections import OrderedDict

""" Part object """

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


# for the 3D version add the orientation in here!