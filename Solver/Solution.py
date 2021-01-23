from Solver.Formatting import *
from Solver.Sorting import *
from solver.Solve import Solve

""" Function that returns a formatted solution """

def Solution(rawPartDict, sheetSize, options = False):
	# options will contain the "randomized b&b" for instance...
	Parts = []
	Sheets = [SheetObject(sheetSize)]	# Start with one
	
	unsortedParts = FormattedInput(rawPartDict)
	
	if options:
		# do something else
	else:
		Areas = [Part.Area for Part in unsortedParts]
		Parts = SortPartObjects(unsortedParts, Areas)
	
	Solve(Parts, Sheets, sheetSize)
		
	return(FormattedOutput(Parts, Sheets))
		