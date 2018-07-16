class set_of_stacks:
	
	def __init__(self):
		self.number_of_stacks = 1
		self.threshold = 3
		self.current = 0
		self.stacks = []
		self.current_stack = []
		
	def _push(self, item):
		if self.current == self.threshold:
			self.stacks.append(self.current_stack)
			self.current = 0
			self.current_stack = []
		self.current_stack.append(item)
		self.current += 1

	def _pop(self):
		if self.number_of_stacks == 1 and self.current == 0:
			return None
		element = self.current_stack.pop()	
		self.current -= 1
		if self.current == 0:
			self.current_stack = self.stacks.pop()
			self.current = self.threshold
		return element

stacks = set_of_stacks()

stacks._push(4)
stacks._push(3)
stacks._push(1)
stacks._push(2)
stacks._push(5)
stacks._push(33)
stacks._push(49)
print stacks.stacks
print stacks._pop()
print stacks._pop()
print stacks._pop()
print stacks._pop()

