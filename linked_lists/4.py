from linked_list import Node

def partition(link_list, x):
	current_node = link_list
	aux_list = None
	aux_list2 = None
	flag = current_node

	while(current_node != None):
		if current_node.data >= x:
			if aux_list == None:
				aux_list = Node(current_node.data)
				aux_list2 = aux_list
			else:
				node = Node(current_node.data)
				aux_list.next = node
				aux_list = aux_list.next	
			flag.next = current_node.next
		else:
			flag = current_node
		current_node = current_node.next

	flag.next = aux_list2
	return link_list

node1 = Node(3)
node2 = Node(5)
node1.next = node2
node3 = Node(8)
node2.next = node3
node4 = Node(5)
node3.next = node4
node5 = Node(10)
node4.next = node5
node6 = Node(2)
node5.next = node6
node7 = Node(1)
node6.next = node7

node1.print_list()
print 'partition'
node1 = partition(node1, 5)
node1.print_list()
