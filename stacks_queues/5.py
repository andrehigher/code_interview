from copy import copy

def sort_stack(stack):
	if len(stack) == 0:
		return []
	aux_stack = []
	while len(stack) > 0:
		elem = stack.pop()
		if len(aux_stack) > 0:
			aux_elem = aux_stack.pop()
			aux_stack.append(aux_elem)
			print aux_elem
		while len(aux_stack) > 0 and elem < aux_elem:
			stack.append(aux_elem)
			aux_elem = aux_stack.pop()
		aux_stack.append(elem)
		print stack
		
	return aux_stack

stack = [8,3,6,12,4,9]
print stack
print sort_stack(stack)
