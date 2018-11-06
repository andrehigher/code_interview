import random 

def kth_largest_element(arr, min, max, k):
	arr[len(arr)/2],arr[max] = arr[max], arr[len(arr)/2]
	pivot_inx = max
	i = min
	j = max
	swap = min
	while i < max:
		if arr[i] < arr[pivot_inx]:
			arr[swap], arr[i] = arr[i], arr[swap]
			swap += 1
		i += 1
	arr[swap], arr[pivot_inx] = arr[pivot_inx], arr[swap]
	print(swap, arr)
	if k == swap-min+1:
		return arr[swap]
	elif k < pivot_inx:
		return kth_largest_element(arr, min, swap-1, k)
	else:
		return kth_largest_element(arr, swap+1, max, k)

def partition1(arr, left, right, pivotIndex):
    arr[right], arr[pivotIndex]=arr[pivotIndex], arr[right]
    pivot=arr[right]
    swapIndex=left
    for i in range(left, right):
        if arr[i]<pivot:
            arr[i], arr[swapIndex] = arr[swapIndex], arr[i]
            swapIndex+=1
    arr[right], arr[swapIndex]=arr[swapIndex], arr[right]
    return swapIndex
 
def kthLargest1(arr, left, right, k):
    if not 1<=k<=len(arr):
        return
    if left==right:
        return arr[left]
 
    while True:
        pivotIndex=random.randint(left, right)
        pivotIndex=partition1(arr, left, right, pivotIndex)
        rank=pivotIndex-left+1
        if rank==k:
            return arr[pivotIndex]
        elif k<rank:
            return kthLargest1(arr, left, pivotIndex-1, k)
        else:
            return kthLargest1(arr, pivotIndex+1, right, k-rank)

print(kthLargest1([3,6,1,2,8,7,10], 0, 6, 4)) 
print(kth_largest_element([3,6,1,2,8,7,10], 0, 6, 4))
