#pag 91
#mxn matrix if element is 0, the entire row and column should be 0 as well

def zero_matrix(matrix):
	n = len(matrix)
	index_i = []
	index_j = []
	for i in range(0, n):
		for j in range(0, len(matrix[i])):
			if matrix[i][j] == 0:
				index_i.append(i)
				index_j.append(j)
	for i in range(0, n):
                for j in range(0, len(matrix[i])):
			if i in (index_i):
				matrix[i][j] = 0
			if j in (index_j):
				matrix[i][j] = 0	
	return matrix

print zero_matrix([[1,2,3,0],[4,5]])
print zero_matrix([[1,2,3,4,5,6,7,8],[10,11,0,12],[13,14,15,16,17],[18,19,20,21]])
print zero_matrix([[1,0,3,4],[0,6,7,8],[9,9,9],[12,23,24,90,98]])
