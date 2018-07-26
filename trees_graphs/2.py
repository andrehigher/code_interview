from tree import Node

def create_tree(tree, element):
	if tree == None:
		return Node(element)
	if element >= tree.value:
		return create_tree(tree.right, element)
	if element < tree.value:
		return create_tree(tree.left, element)

def minimal_tree(arr):
	if arr == None or len(arr) == 0:
		return None
	if len(arr) == 1:
		return create_tree(None, arr[0])

	root = create_tree(None, arr[ (len(arr) / 2)])
	root.right = minimal_tree(arr[(len(arr) / 2)+1:])
	root.left = minimal_tree(arr[:(len(arr) / 2)])
	return root

def pre_order(tree):
	if tree == None:
		return False
	print tree.value
	pre_order(tree.left)
	pre_order(tree.right)

actual_tree = minimal_tree([1,2,3,4,5,6])
pre_order(actual_tree)
