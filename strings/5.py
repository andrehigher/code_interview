def one_way(string1, string2):
	if string1 == string2:
		return True
	hash = [0 for _ in range(27)]
	for i in range(0, max(len(string1),len(string2))):
		if i < len(string1):
			hash[ord(string1[i])-97] += 1
                if i < len(string2):
			hash[ord(string2[i])-97] -= 1
		
	is_more_way = 0
	for i in range(0, len(hash)):
		if hash[i] != 0:
			is_more_way += 1

	if is_more_way > 2:
		return False
	else:
		return True

print one_way('pale', 'ple')
print one_way('pales', 'pale')
print one_way('pale', 'bale')
print one_way('pale', 'bake')
print one_way('apple', 'aple')
