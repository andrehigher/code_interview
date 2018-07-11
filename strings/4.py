def palindrome_permutation(string):
	sorted_string = sorted(string)
	permutation = False
	is_odd = False
	count = 0
	letter = ""
	for i in range(0, len(string)):
		if sorted_string[i] != " ":
			if letter == sorted_string[i]:
				count += 1
			else:
				if count % 2 != 0:
					if is_odd == True:
						return False
					else:
						is_odd = True

				letter = sorted_string[i]
				count = 1

	return True	

print palindrome_permutation("tactcoapapa")
