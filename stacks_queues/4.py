from copy import copy

class my_queue:

	def __init__(self):
		self.stack1 = []
		self.stack2 = []

	def _push(self, item):
		self.stack1.append(item)
		aux = copy(self.stack1)
		self.stack2 = []
		for i in range(len(self.stack1)):
			elem = aux.pop()
			self.stack2.append(elem)

	def get_first(self):
		aux = copy(self.stack1)
		aux2 = []
		for i in range(len(aux)):
			elem = aux.pop()
			aux2.append(elem)
		aux2.pop()
		self.stack1 = []
		for i in range(len(aux2)):
			elem = aux2.pop()
			self.stack1.append(elem)
		return self.stack2.pop()

	def get_last(self):
		aux = copy(self.stack2)
                aux2 = []
                for i in range(len(aux)):
                        elem = aux.pop()
                        aux2.append(elem)
                aux2.pop()
                self.stack2 = []
                for i in range(len(aux2)):
                        elem = aux2.pop()
                        self.stack2.append(elem)
		return self.stack1.pop()
			
			
my = my_queue()
my._push(1)
my._push(2)
my._push(3)
my._push(4)


print my.stack1
print my.stack2
#print my.get_first()
print my.get_last()
print my.stack1
print my.stack2
