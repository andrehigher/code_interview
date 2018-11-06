def find_word_row(matrix, word, i, j):
	count = 0
	if len(word) > (len(matrix[0])-j):
		return False

	for a in range(j, len(matrix[0])):
		if count < len(word) and word[count] != matrix[i][a]:
			return False
		count += 1
		
	return True

def find_word_column(matrix, word, i, j):
	count = 0
	if len(word) > (len(matrix)-i):
		return False

	for b in range(i, len(matrix)):
		if count < len(word) and word[count] != matrix[b][j]:
			return False
		count += 1

	return True

def crossword(matrix, word):
	if len(matrix) == 0 or word == '':
		return True

	for i in range(0, len(matrix)):
		for j in range(0, len(matrix[0])):
			if word[0] == matrix[i][j]:
				#start point
				if find_word_row(matrix, word, i, j):
					return True
				if find_word_column(matrix, word, i, j):
					return True

	return False


matrix = [
		['a', 'p', 'p', 'l', 'e', 'a'],
		['a', 'p', 'l', 'e', 'z', 'r'],
		['b', 'u', 'p', 'o', 'y', 'g']
	]
result = crossword(matrix, 'ap1le')
print(result)
