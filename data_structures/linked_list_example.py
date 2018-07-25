from linked_list import Node

print 'creating linked list'
first = Node(1)
print 'inserting second element'
second = Node(2)
first.next = second
print 'inserting third element'
third = Node(3)
second.next = third
print 'inserting fourth element'
fourth = Node(4)
third.next = fourth
print 'printing linked list'

aux = first
while aux != None:
	print aux.value
	aux = aux.next
