from collections import OrderedDict
from Formatting import *
from Processes.Sorting import *
from Solve import Solve
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
		return("this functionality hasn't been configured yet.")
	else:
		Parts = sorted(unsortedPartObjects, key=lambda part: part.Area, reverse = True) 
		
	Solve(Parts, Sheets, problemParameters)
		
	return(FormattedOutput(Parts, Sheets, problemParameters))
		