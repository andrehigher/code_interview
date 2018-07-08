from linked_list import Node

def return_kth(link_list, k, final_list):
	current_node = link_list
	if link_list != None:
		count = return_kth(link_list.next, k, final_list) - 1
		if count >= 0:
			final_list.append(link_list.data)
		return count
	else:
		return k

node1 = Node(1)
node2 = Node(2)
node1.next = node2
node3 = Node(3)
node2.next = node3
node4 = Node(4)
node3.next = node4
node5 = Node(5)
node4.next = node5

final_list = []
return_kth(node1, 3, final_list)
print final_list
