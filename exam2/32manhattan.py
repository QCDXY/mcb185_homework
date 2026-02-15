def manhattan(X1,X2):
	if len(X1) != len(X2):
		return 'List do not have same length.'
	total = 0
	for index,value in enumerate(X1):
		total += abs(X1[index]-X2[index])
	return total
	
print(manhattan([1,2,3],[1,2,3]))
print(manhattan([4,5,6],[1,2,3]))
