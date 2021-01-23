from SolverObjects.Processes.Formatting import *
from SolverObjects.Processes.Sorting import *
from Solver.Solve import Solve
from SolverObjects.Parameters import Parameters

""" Function that returns a formatted solution """

def Solution(rawPartDict, sheetSize, options = False):
	# options could signal the "randomized b&b" for instance...
	problemParameters = Parameters(sheetSize)
	Parts = []
	Sheets = []	
	unsortedPartObjects = FormattedInput(rawPartDict)
	
	if options:
		# do something else
	else:
		Areas = [Part.Area for Part in unsortedParts]
		Parts = SortPartObjects(unsortedParts, Areas)
	
	Solve(Parts, Sheets, problemParameters)
		
	return(FormattedOutput(Parts, Sheets, problemParameters))
		