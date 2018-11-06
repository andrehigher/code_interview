def array_pair_sum(arr, k):
	arrSorted = sorted(arr)
	i = 0
	j = len(arr) - 1
	result = set()
	while i < j:
		temp = arrSorted[i] + arrSorted[j]
		if temp == k:
			result.add((arrSorted[i], arrSorted[j]))
			i += 1
		elif temp > k:
			j -= 1
		else:
			i += 1 	
	print(result)

array_pair_sum([1,2,12,4,3,5,8,6,7,9], 10)
