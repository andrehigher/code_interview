from collections import deque

a = deque([])
print 'appending 1'
a.append(1)
print 'appending 2'
a.append(2)
print 'appending 3'
a.append(3)
print 'dequeing an element'
print a.popleft()
print 'appending 4'
a.append(4)
print 'dequeing an element'
print a.popleft()
