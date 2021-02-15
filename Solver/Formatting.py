from SolverObjects.PartObject import PartObject
from collections import OrderedDict
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
	
	originalOrderPartsList = sorted(reOrderedPartObjects, key=lambda part: part.Index)
	
	partOutput = [Part.FormatOutput(parameters) for Part in originalOrderPartsList]
	sheetOutput = [Sheet.Coordinates for Sheet in sheetObjects]
	
	partsAndSheets = OrderedDict([('parts',partOutput),('sheets',sheetOutput)])
	formattedOutput = OrderedDict([("results",partsAndSheets)])
	return(json.dumps(formattedOutput))
	

