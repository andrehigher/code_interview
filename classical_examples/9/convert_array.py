def getIndex(currentIndex, N):
 	return (currentIndex%3)*N + (currentIndex/3)
 
def convertArray_extraSpace(arr):
 	N=len(arr)/3
 	return [arr[getIndex(i, N)] for i in range(len(arr))]

def convert_array(arr):
	N = len(arr)/3
	for currentIndex in range(len(arr)):
		swapIndex = getIndex(currentIndex, N)
		while swapIndex < currentIndex:
			swapIndex = getIndex(swapIndex, N)
		arr[currentIndex], arr[swapIndex] = arr[swapIndex], arr[currentIndex]
	return arr
		

print(convertArray_extraSpace([1,2,3,4,5,6,7,8,9,10,11,12]))
print(convert_array([1,2,3,4,5,6,7,8,9,10,11,12]))
