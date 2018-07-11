def find_longest_substring(string, list_strings):
	string = sorted(string)
	string1 = ""
	for i in range(0, len(list_strings)):
		list_strings[i] = sorted(list_strings[i])
		is_substring = True
		for j in range(0, len(list_strings[i])):
			if list_strings[i][j] != string[j]:
				is_substring = False	
		if is_substring == True and len(string1) < len(list_strings[i]):
			string1 = list_strings[i]
	return string1
print find_longest_substring("abppplee", ["able", "ale", "apple", "bale", "kangaroo"])
