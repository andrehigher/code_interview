steps_available = 2

def find_bugs_row_reverse(matrix, i, j):
        bugs = 0
        steps = 0
        for a in range(j, -1):
                steps += 1
                if matrix[i][a] == 2:
                        bugs += 1
                if steps > steps_available or matrix[i][a] == 1:
                        break
        return bugs

def find_bugs_row(matrix, i, j):
	bugs = 0
	steps = 1
	for a in range(j, len(matrix[0])):
		steps += 1
		if matrix[i][a] == 2:
			bugs += 1
		if steps > steps_available or matrix[i][a] == 1:
			break
	return bugs

def find_bugs_column_reverse(matrix, i, j):
        bugs = 0
        steps = 1
        for a in range(i, -1):
                steps += 1
                if matrix[a][j] == 2:
                        bugs += 1
                if steps > steps_available or matrix[a][j] == 1:
                        break
        return bugs

def find_bugs_column(matrix, i, j):
        bugs = 0
        steps = 1
        for a in range(i, len(matrix)):
                steps += 1
                if matrix[a][j] == 2:
                        bugs += 1
                if steps > steps_available or matrix[a][j] == 1:
                        break
        return bugs

def bugs(matrix):
	max_bugs = None
	max_index = (None, None)
	for i in range(len(matrix)):
		for j in range(len(matrix[0])):
			amount_bugs = 0
			# available spot
			if matrix[i][j] == 0:
				amount_bugs = find_bugs_row(matrix, i, j)
				amount_bugs += find_bugs_row_reverse(matrix, i, j)
				amount_bugs += find_bugs_column(matrix, i, j)
				amount_bugs += find_bugs_column_reverse(matrix, i, j)
				print((i,j), amount_bugs)
				if amount_bugs > max_bugs:
					max_bugs = amount_bugs
					max_index = (i, j)

	return max_index
matrix = [
		[ 0, 0, 0, 0, 0, 0 ],
		[ 0, 0, 2, 1, 0, 0 ],
		[ 0, 1, 0, 0, 1, 0 ],
		[ 0, 2, 0, 1, 0, 2 ],
		[ 0, 2, 0, 2, 0, 0 ]
	 ]
print(bugs(matrix))
