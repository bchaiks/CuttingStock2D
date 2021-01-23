"""
Functions for computing merit of particular positions
"""

def BoundingBox(newPart, candidatePositionIndex, sheet):
		
		candidatePosition = sheet.extremePoints[candidatePositionIndex]
		D = Dims
		CI = curr_items
		CE = curr_eps

		X = candidatePosition[0] + newPart.Dim[0]
		Y =  candidatePosition[1] + newPart.Dim[1]
		
		for i in range(len(sheet.currentParts)):
		
			currentPart = sheet.currentParts[i]
			
			if currentPart.Position[0] + currentPart.Dim[0] > X:
				X = currentPart.Position[0] + currentPart.Dim[0]
			
			if currentPart.Position[1] + currentPart.Dim[1] > Y:
				Y = currentPart.Position[1] + currentPart.Dim[1]
		
		val = X*Y + X 	# Slightly penalizing things far in the X dimension
		
		return(val)