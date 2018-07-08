def rotate_matrix(matrix):
	n = len(matrix)
	if n == 0:
		return []

	print matrix
	for i in range(0, (n/2)):
		first = i
		last = n - 1 - i
		for j in range(first, last):
			offset = j - first
			
			# save top
			top = matrix[first][j]
			
			# right -> top
			matrix[first][j] = matrix[j][last]

			# bottom -> right
			matrix[j][last] = matrix[last][last - offset]

			# left -> bottom
			matrix[last][last - offset] = matrix[last - offset][first]

			# top -> left
			matrix[last - offset][first] = top
	return matrix

print rotate_matrix([[1,2],[3,4]])
print rotate_matrix([[1,2,3],[4,5,6],[7,8,9]])
print rotate_matrix([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
