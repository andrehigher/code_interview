def string_compression(string):
	if len(string) == 0:
		return ''
	current_letter = string[0]
	new_string = ''
	count = 1
	for i in range(1, len(string)):
		if string[i] != current_letter:
			new_string += current_letter + str(count)
			current_letter = string[i]
			count = 1
		else:
			count += 1

	new_string += current_letter + str(count)
	if len(new_string) >= len(string):
		return string
	else:
		return new_string

print string_compression('')
print string_compression('aabcccccaaa')
print string_compression('aaBBbccAAAAAAccccc')
print string_compression('sasa')
