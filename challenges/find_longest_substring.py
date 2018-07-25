def find_longest_substring(string, list_strings):
	string1 = ""
	for i in range(0, len(list_strings)):
		k = 0
		for j in range(0, len(string)):
			if list_strings[i][k] == string[j]:
				k += 1
			if len(list_strings[i]) <= k:
				break
		if len(string1) < k and k == len(list_strings[i]):
			string1 = list_strings[i]
	return string1
print find_longest_substring("abppplee", ["able", "ale", "apple", "bale", "kangaroo"])
print find_longest_substring("abpcplea", ['ale', 'apple', 'monkey', 'plea'])
print find_longest_substring("abpcpleeaDChsssgtrsssmonkey", ['ale', 'applee', 'monkey', 'plea'])
