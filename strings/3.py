def URLify(string):
	new_string = ""
	for i in range(0, len(string)):
		if string[i] != " ":
			new_string += string[i]
		else:
			new_string += "%20"
	return new_string

print URLify("Andre Gonzaga")
