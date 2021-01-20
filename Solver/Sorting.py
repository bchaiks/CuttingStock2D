"""
Part ordering -- EVENTUALLY INCLUDE RANDOMIZED ETC...
"""


def NonIncreasingOrder(tuples, specificValues):
	'''e.g. parts by area or volume, or PartObjects by position in list'''
	orderedTuples = [i for _,i in sorted(zip(specificValues, tuples), reverse = True)]
	return(orderedTuples)

def SortArrayByArgMinIndex(array,index):
	'''
	Sorts a multi_dim array by index that minimizes certain entry
	MAKE SURE TO SORT BY MOST IMPORTANT INDEX LAST!!!
	'''
	a = array
	L = len(a)
	for i in range(L):
		temp = a[i]
		flag = 0
		j = 0
		while j < i and flag == 0:
			if temp[index] < a[j][index]:
				a[j+1] = a[j]
				a[j] = temp
				j += 1
			else:
				flag = 1
	return(a)

def UniqueValues(array):
	''' return unique values of an array '''
	u_a = []
	L = len(array)
	for i in range(L):
		if array[i] in u_a:
			continue
		else:
			u_a.append(array[i])
	return(u_a)
