def stack_min(stack):
	aux = []
	min = 99999999
	for i in range(0,len(stack)):
		number = stack.pop()
		if min > number:
			min = number
		aux.append(number)
	print aux
	for i in range(0, len(aux)):
		number = aux.pop()
		stack.append(number)
	print stack
	return min

print stack_min([1,2,3,4])
