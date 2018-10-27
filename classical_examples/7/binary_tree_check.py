class Tree:
	def __init__(self, value):
		self.value = value
		self.right = None
		self.left = None

root = Tree(3)
first = Tree(2)
root.left = first
second = Tree(1)
first.left = second
third = Tree(4)
first.right = third
fourth = Tree(5)
root.right = fourth

def in_order(tree):
	if tree == None:
		return False
	in_order(tree.left)
	print tree.value
	in_order(tree.right)

in_order(root)


def check_binary_tree(root, min_value, max_value):
	if root == None:
		return True
	
	if not min_value <= root.value <= max_value:
		return False

	return check_binary_tree(root.left, min_value, root.value) and check_binary_tree(root.right, root.value, max_value)

INFINITY = float("infinity")
NEG_INFINITY = float("-infinity")
print(check_binary_tree(root, NEG_INFINITY, INFINITY))
