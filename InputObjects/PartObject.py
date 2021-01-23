"""
Part object

Stores: 
- dimensions
- name 
- positionInList: the ORIGINAL list of parts given
- sheet number 
- coordinate of lower left corner

"""

class PartObject:
	def __init__(self, dimensions, label, positionInInputList):
	'''
	positionInList is the ORDER THE PARTS ARE GIVEN TO THE ROUTINE!
	'''
		self.Dim = dimensions
		self.Area = self.Dim[0]*self.Dim[1]
		self.Label = label
		self.Index = positionInInputList
		
		# these get instantiated during the process
		# index of sheet where part is positioned
		self.SheetIndex = None
		# Actual coordinate of placement function of the placement ant 
		# the sheet index...
		self.LowerLeftCoordinate = None
		# index of extreme point in SheetObject.extremePoints 
		# (for use in the algorithm)  -- i.e. this will get the 
		# e_cand index within the algorithm...
		self.ExtremePointIndex = None

'''
Will be able to format the final position 
using the SheetIndex, sheetSize, and margin inputs... 
'''

# for the 3D version add the orientation in here!