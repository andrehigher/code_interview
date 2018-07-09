from linked_list import Node

def sum_lists(list1, list2, sum_list, exceed):
	if list1 == None and list2 == None:
		return None

	value = 0
	if list1 != None:
		value += list1.data

	if list2 != None:
		value += list2.data

	if sum_list == None:
		sum_list = Node( ((value + exceed) % 10) )
	else:
		sum_list.next = Node( ((value + exceed) % 10) )
		if (list1 != None and list1.next == None) and (list2 != None and list2.next == None) and (((value + exceed) / 10) > 0):
			sum_list = sum_list.next
			sum_list.next = Node(1)
			
		sum_list = sum_list.next

	if list1 != None:
		list1 = list1.next
	if list2 != None:
		list2 = list2.next
	sum_lists(list1, list2, sum_list, ((value + exceed) / 10))
	return sum_list

list1 = Node(5)
node2 = Node(9)
list1.next = node2
node3 = Node(3)
node2.next = node3
node6 = Node(3)
node3.next = node6

list2 = Node(2)
node4 = Node(4)
list2.next = node4
node5 = Node(7)
node4.next = node5

sum_list = sum_lists(list1, list2, None, 0)
sum_list.print_list()
