def is_unique(string):
	string_sorted = sorted(string)
	for i in range(0, len(string)-1):
		if string_sorted[i] == string_sorted[i+1]:
			return True
	return False

print is_unique("andre");
