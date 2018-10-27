def matrix_region_sum(matrix, X, Y):
	result = 0
	if len(matrix) == 0:
		print 'matrix empty'
		return False
	for i in range(X[0], Y[0] + 1):
		for j in range(X[1], Y[1] + 1):
			result += matrix[i][j]	

	print(result)

matrix = [[1,2,3],[4,5,6],[7,8,9]]
X = [0,0]
Y = [1,1]
matrix_region_sum(matrix,X,Y)
