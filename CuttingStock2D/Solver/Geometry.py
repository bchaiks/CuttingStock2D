"""
Functions for positioning geometry
"""

def CheckPositionFeasibility(candidatePosition, sheet, part):
	

def Feas(Dims, EP, Bin_Size, Curr_items, Curr_EP):
	'''
	Returns True if a piece of dimension 
	Dims = WxD is feasible in a bin with leftmost corner at EP 

	Bin_Size = 1x2 dimensions of bin
	Dims = 1x2
	EP = 1x2 -- coordinates of the chosen spot

	For all items in Curr_items placed at Curr_Ep
	have to make sure that EP[0] + d[OR[0]] doesn't 
	poke through... item[j][0] -- item[j][0] + Curr_Ep[j][0]	
	'''
	BS = Bin_Size
	D = Dims
	CI = Curr_items
	CE = Curr_EP
	check = True	
	for i in range(2):
		# Bin limits
		if D[i] + EP[i] > BS[i]:
			check = False
		
	for j in range(len(CI)):
		# checking intersections with other items

		for k in range(2):
			a = (k + 1)%2
		
			if overlap(D,EP,CI[j],CE[j],k,a,): 
				check = False
	return check

def overlap(d1,c1, d2,c2, k,x):
	'''
	returns True if two 3-d boxes with dimensions d1 d2
	and lower left corners c1, c2 overlap on the x dim...
	'''	
	ov = True
	if c1[x] >= c2[x] + d2[x]:
		ov = False
	if c2[x] >= c1[x] + d1[x]:
		ov = False
	
	if c1[k] >= c2[k] + d2[k]:
		ov = False
	if c2[k] >= c1[k] + d1[k]:
		ov = False
	return ov
		
		
def proj(d1,e1,d2,e2, proj_dir):
	'''
	d1, e1 -- dim of new piece, placed at point e1
	d2, e2 -- cycle these through the other pieces

	ep_dir is the coordinate "pushed out" by the piece dimension in 
	the candidate extreme point
	proj_dir is the one to shrink... (number 0,1 corresponding to x, y)
	'''

	pd = proj_dir
	# remaining dimension???	
	od = 1-pd
	check = True

	if d2[pd] + e2[pd] > e1[pd] :
		#i.e. piece is further from axis in projection direction 
		check = False

	if  e2[od] > e1[od]:
		#i.e. piece too far
		check = False
	if e2[od] + d2[od] < e1[od] :
		# i.e. piece not far enough
		check = False
	return check

def Update_EP(Dims, EP, Curr_EPs, Curr_Items, piece_margin):
	'''
	Dims = 1x2 WxD of current piece placed 
		(in orienation OR* decided by Feas and Merit...)
	EP = 1x2 coordinates of lower left corner of current piece
	Curr_EPs = list of current extreme points where Curr_Items
		are located 
	Curr_Items = list of dimensions of current items 

	idea is you take current EP and push it out in the 
	two dimensions of the current piece, then project
	each of these towards the other axes, ending up 
	on the closest current piece it "runs into"

	'''
	p_m = piece_margin
	D = Dims
	CI = Curr_Items
	CE = Curr_EPs
	New_Eps = [[EP[0]+D[0] + p_m,EP[1]],
				[EP[0],EP[1]+D[1] + p_m]]

	Max_bounds = [-1., -1. ]

	for i in range(len(CI)):
		# shrinking y coordinate
		if proj(D, EP, CI[i], CE[i],1) and CE[i][1] + CI[i][1] + p_m > Max_bounds[1]:
			New_Eps[0] = [EP[0] + D[0] + p_m, CE[i][1] + CI[i][1] + p_m]
			Max_bounds[0] = CE[i][1] + CI[i][1] + p_m
		

		# shrinking x coordinate
		if proj(D, EP, CI[i], CE[i],0) and CE[i][0] + CI[i][0] + p_m > Max_bounds[0]:
			New_Eps[1] = [CE[i][0] + CI[i][0] + p_m, EP[1] + D[1] + p_m]
			Max_bounds[1] = CE[i][0] + CI[i][0] + p_m	
		
	# remove duplicates
	#New_Eps = unq(New_Eps)
	return (unq(New_Eps))
