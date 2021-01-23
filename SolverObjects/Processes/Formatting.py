from InputObjects.PartObject import PartObject
from InputObjects.SheetObject import SheetObject
from Solver.Sorting import SortPartObjects

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
	
	originalPartOrder = [Part.Index for Part in partObjects] 
	originalPartsList = [i for _,i in sorted(zip(originalPartOrder, partObjects))]
	
	
	output = []
	for part in originalPartsList:
		result = {'part': part.Label, 'x': part.Position[0] }
		output.append()
	
	outputDict = json.dumps({"results":{'parts': output, 'sheets': SheetCoordinates}})
	
	return( outputDict)
	
	
	Result = [ptp[p][2],{'part': ptp[p][0], 'x': Cr_EPs[c][L-1][0]+margin , 'y': Cr_EPs[c][L-1][1]+ margin + (5+ Actual_dim[1])*packed_in}]
	
	originalPartOrder = [Part.Index for Part in partObjects] 
	originalPartsList = [i for _,i in sorted(zip(originalPartOrder, partObjects))]
	
	
	Sheet_coord = []

	for i in range(len(SH)):
		y = (5+ Actual_dimD[1])*i
		x = 0
		entry = {'sheet': i, 'x': x, 'y':y}
		Sheet_coord.append(entry)


	# re_order packing
	output = []
	for i in range(len(parts)):
		for j in range(len(parts)):
			if Packings[j][0] == i:
				output.append(Packings[j][1])

    OUTPUT = json.dumps({"results":{'parts': output,
                'sheets': Sheet_coord}})
    return OUTPUT
