#pag 91
# string1 and string2, check if string2 is a rotation of s1 using only one call to isSubstring ("waterbottle" is a rotaton of "erbotthewat")

def string_rotation(string1, string2):
	# O( n log n)
	#str1_sorted = sorted(string1)
	#str2_sorted = sorted(string2)
	#str1_sorted = "".join(str1_sorted)
	#str2_sorted = "".join(str2_sorted)
	#print str1_sorted
	#print str2_sorted
	#if str2_sorted in str1_sorted or str1_sorted == str2_sorted:
	#	return True
	#else:
	#	return False

	# O (n)
	string2 = string2 + string2
	return string1 in string2

print string_rotation("erbottlewat", "waterbottle")
print string_rotation("erbotthewat", "sadf")
