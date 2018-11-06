def preCompute(matrix):
	topRow, bottomRow = ( 0, len(matrix)-1 )
	leftCol, rightCol = ( 0, len(matrix[0])-1 )

	sum=[[0]*(rightCol-leftCol+1) for i in range(bottomRow-topRow+1)]
	sum[topRow][leftCol] = matrix[topRow][leftCol]

	for col in range(leftCol+1, rightCol+1):
		sum[topRow][col] = sum[topRow][col-1]+matrix[topRow][col]
	for row in range(topRow+1, bottomRow+1):
		sum[row][leftCol] = sum[row-1][leftCol]+matrix[row][leftCol]

	for col in range(leftCol+1, rightCol+1):
		columnSum=matrix[topRow][col]
		for row in range(topRow+1, bottomRow+1):
			sum[row][col] = sum[row][col-1]+matrix[row][col]+columnSum
			columnSum+=matrix[row][col]
	return sum


def matrix_region_sum(matrix, X, Y, sum):
	if len(matrix) == 0:
		return 0
	
	if X[0] == 0 or X[1] == 0:
		OA = 0
	else:
		OA = sum[X[0]-1][X[1]-1]

	if X[1] == 0:
		OC = 0
	else:
		OC = sum[Y[0]][X[1]-1]

	if X[0] == 0:
		OB = 0
	else:
		OB = sum[X[0]-1][X[1]]

	OD = sum[Y[0]][Y[1]]
	
	return OD-OB-OC+OA
		
matrix = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]
sum = preCompute(matrix)
print(matrix_region_sum(matrix, [2,2], [4,4], sum))
