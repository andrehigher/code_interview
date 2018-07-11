def is_permutation(string1, string2):
	string1_sorted = sorted(string1)
	string2_sorted = sorted(string2)
	if string1_sorted == string2_sorted:
		return True
	return False

print is_permutation('asdasds', 'aassdd')
