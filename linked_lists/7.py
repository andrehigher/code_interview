from linked_list import Node

def intersection(list1, list2):
	len1 = 0
	current_node1 = list1
	while current_node1.next != None:
		len1 += 1
		current_node1 = current_node1.next

	len2 = 0
	current_node2 = list2
	while current_node2.next != None:
		len2 += 1
		current_node2 = current_node2.next

	if current_node1 != current_node2:
		return False
	
	current_node1 = list1
	current_node2 = list2
	print current_node1, current_node2
	if len1 > len2:
		count = 0
		while count != len1:
			current_node1 = current_node1.next
			count += 1
	elif len2 > len1:
		count = 0
		while count != len2:
			current_node2 = current_node2.next
			count += 1

	
	while current_node1 != current_node2:
		current_node1 = current_node1.next
		current_node2 = current_node2.next
		
	return current_node1

list1 = Node(1)
node2 = Node(2)
list1.next = node2
node3 = Node(3)
node2.next = node3

list2 = Node(1)
node4 = Node(3)
list2.next = node4
node5 = Node(5)
node4.next = node5
node5.next = node2

print intersection(list1, list2)
