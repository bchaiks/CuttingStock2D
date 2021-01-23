from InputObjects.PartObject import PartObject
from InputObjects.SheetObject import SheetObject

""" Functions for formatting input and output """

def FormattedInput(inputPartDict):
	
	Labels = list(inputPartDict.keys())
	partObjects = []
	
	for i in range(len(Labels)):
		Dims = inputPartDict[Labels[i]]
		partObjects.append(PartObject(Dims, Labels[i],i))
		
	return(partObjects)	
	
	
def FormattedOutput(partObjects, sheetObjects):
	# format output from arrays of 
	# PartObjects and SheetObjects RESULTING 
	# FROM the algorithm...
	
	return( OutputDict...)