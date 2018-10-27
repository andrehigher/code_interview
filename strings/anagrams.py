def anagram(arr):
	dicti = {}
	
	for word in arr:
		temp = word
		aux = ''.join(sorted(temp))
		if aux not in dicti:
			dicti[aux] = [word]
		else:
			dicti[aux].append(word)
	print(dicti)

print(anagram(['star', 'car', 'rats', 'bla', 'blue', 'sart', 'rac', 'a'])) 
		
