"""
Part object

Stores: 
- dimensions
- name 
- position in the ORIGINAL list of parts given
- sheet number 
- coordinate of lower left corner

"""

class PartObject:
	def __init__(self, dimension, name, positionInList):
		self.Dim = dimension
		self.Name = name
		self.Index = positionInList
		
		# these get instantiated during the process
		self.SheetIndex = None
		self.LowerLeftCoordinate = None

'''
Will be able to format the final position 
using the SheetIndex, sheetSize, and margin inputs... 
'''

# for the 3D version add the orientation in here!