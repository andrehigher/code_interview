from linked_list import Node

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

