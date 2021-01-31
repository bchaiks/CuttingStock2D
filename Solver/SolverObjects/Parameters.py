""" 
Parameters object - change or overwrite edge/part/sheetMargin if necessary
"""
class Parameters:
	edgeMargin = 1.0
	partMargin = 1.0
	sheetMargin = 5.0
	
	def __init__(self, sheetSize):
		self.sheetSize = sheetSize
