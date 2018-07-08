from linked_list import Node

def remove_dups(linked_list):
	unique = []
	flag = linked_list
	current_node = linked_list
        while(current_node.next != None):
        	if current_node.data not in unique:
			unique.append(current_node.data)
			flag = current_node
			current_node = current_node.next
		else:
			flag.next = current_node.next
			current_node = flag.next

	if current_node.data in unique:
                flag.next = None
				

node1 = Node(1)
node2 = Node(2)
node1.next = node2
node3 = Node(3)
node2.next = node3

node1.remove_node(2)
node2 = Node(2)
node3.next = node2
node4 = Node(4)
node2.next = node4
node1_rep = Node(1)
node4.next = node1_rep
node4_rep = Node(4)
node1_rep.next = node4_rep
node1.print_list()

print 'Removing duplication'
#node1.remove_node(1)
remove_dups(node1)
node1.print_list()
