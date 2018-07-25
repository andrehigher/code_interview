from tree import Node

def insert_node(tree, element):
	if tree.value <= element and tree.right == None:
		tree.right = Node(element)
		return True
	if tree.value > element and tree.left == None:
		tree.left = Node(element)
		return True
	if tree.value <= element:
		return insert_node(tree.right, element)
	if tree.value > element:
		return insert_node(tree.left, element)

def in_order(tree):
	if tree == None:
		return False
	in_order(tree.left)
	print tree.value
	in_order(tree.right)

def pre_order(tree):
	if tree == None:
		return False
	print tree.value
	pre_order(tree.left)
	pre_order(tree.right)

def post_order(tree):
	if tree == None:
		return False
	post_order(tree.right)
	print tree.value
	post_order(tree.left)



print 'creating tree'
tree = Node(5)
aux = tree
print 'inserting 2'
insert_node(aux, 2)
aux = tree
print 'inserting 6'
insert_node(aux, 6)
aux = tree
print 'inserting 1'
insert_node(aux, 1)
aux = tree
print 'inserting 3'
insert_node(aux, 3)
aux = tree
print 'inserting 18'
insert_node(aux, 18)
aux = tree
print 'printing tree in in order'
in_order(aux)
aux = tree
print 'printing tree in pre order'
pre_order(aux)
aux = tree
print 'printing tree in post order'
post_order(aux)
