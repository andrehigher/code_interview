from linked_list import Node

def palindrome(link_list, stack):
	if link_list == None:
		i = 0
		j = len(stack) - 1
		while(i <= j):
			if stack[i] != stack[j]:
				return False			
			i += 1
			j -= 1
		return True

	stack.append(link_list.data)
	return palindrome(link_list.next, stack)

node1 = Node('a')
node2 = Node('b')
node1.next = node2
node3 = Node('a')
node2.next = node3
#node4 = Node('a')
#node3.next = node4


print palindrome(node1, [])
