def largest_sum(arr):
	if len(arr) == 0:
		return 0

	maxSum=currentSum=arr[0]
	for elem in arr[1:]:
		currentSum = max(elem,currentSum+elem)
		maxSum = max(maxSum, currentSum)
	return maxSum

arr = [-1,-2,-3,-4,-5,-6]
print(largest_sum(arr))

