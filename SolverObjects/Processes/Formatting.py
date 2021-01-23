from SolverObjects.PartObject import PartObject
import json

""" Functions for formatting input and output """

def FormattedInput(inputPartDict):
	
	Labels = list(inputPartDict.keys())
	partObjects = []
	
	for i in range(len(Labels)):
		Dims = inputPartDict[Labels[i]]
		partObjects.append(PartObject(Dims, Labels[i], i))
		
	return(partObjects)	
	
	
def FormattedOutput(reOrderedPartObjects, sheetObjects, parameters):
	
	originalPartOrderIndices = [Part.Index for Part in reOrderedPartObjects] 
	originalOrderPartsList = [i for _,i in sorted(zip(originalPartOrderIndices, partObjects))]
	
	partOutput = [Part.FormatOutput(parameters) for Part in originalOrderPartsList]
	sheetOutput = [Sheet.Coordinates for Sheet in sheetObjects]
	
	formattedOutput = json.dumps({"results":{'parts': partOutput, 'sheets': sheetOutput}})
	
	return(formattedOutput)
	

