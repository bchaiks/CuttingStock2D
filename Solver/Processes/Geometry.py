""" Functions for positioning geometry """

def CheckFeasibility(newPart, candidatePositionIndex, sheet):
	
	candidatePosition = sheet.extremePoints[candidatePositionIndex]
	check = True	
	
	for i in range(2):		# check if violate sheet limits
		if newPart.Dim[i] + candidatePosition[i] > sheet.useableSize[i]:
			check = False	
	for j in range(len(sheet.currentParts)):	# check if overlap with current parts
		if overlap(newPart,candidatePosition, sheet.currentParts[j]): 
			check = False
			
	return check


def overlap(Part1, position, Part2):

	ov = True
	
	if position[0] >= Part2.Dim[0] + Part2.Position[0]:
		ov = False
	if Part2.Position[0] >= position[0] + Part1.Dim[0]:
		ov = False
	if position[1] >= Part2.Dim[1] + Part2.Position[1]:
		ov = False
	if Part2.Position[1] >= position[1] + Part1.Dim[1]:
		ov = False
		
	return ov
		
		
def TakesProjection(Part1, Part2, proj_dir):
	
	pd = proj_dir	
	od = 1-pd
	check = True

	if Part2.Dim[pd] + Part2.Position[pd] > Part1.Position[pd]:
		#i.e. piece is further from axis in projection direction 
		check = False
	if  Part2.Position[od] > Part1.Position[od]:
		#i.e. piece too far
		check = False
	if Part2.Position[od] + Part2.Dim[od] < Part1.Position[od] :
		# i.e. piece not far enough
		check = False
	return check

