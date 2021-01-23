"""
Solution Object
"""
from Solver.Formatting import *
from Solver.Sorting import *

def Solution(self, rawPartDict, options = False):
	# options will contain the "randomized b&b" for instance...

	unsortedParts = FormattedInput(rawPartDict)
	Areas = [Part.Area for Part in unsortedParts]
	Parts = []
	if options:
		# do something else
	else:
		Parts = SortPartObjects(unsortedParts,Areas)

	# place them in the bins according to merit and feasibility,
	# return the FORMATTED OUTPUT
	
	# loop through sheets and open extreme points
		
	return(FormattedOutput(Parts, Sheets))
		