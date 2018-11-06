def findMissingElement(array1, array2):
	array1.sort()
	array2.sort()
	for i in range(0, min(len(array1),len(array2))):
		if array1[i] != array2[i]:
			if len(array1) > len(array2):
				return array1[i]
			else:
				return array2[i]

	return 0

def findMissingElement2(array1, array2):
	dicti = {}
	for elem in array1:
		if elem in dicti:
			dicti[elem] += 1
		else:
			dicti[elem] = 1
	
	for elem in array2:
		if elem in dicti:
			dicti[elem] -= 1
		else:
			dicti[elem] = 1

	for key,value in dicti.items():
		if value > 0:
			return key

	return 0

print(findMissingElement([1,2,3,4,5],[2,5,3,1]))
print(findMissingElement2([1,2,3,4,5],[2,5,3,1]))
