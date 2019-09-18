
class Solution(object):
	
	def __init__(self):
		self.queue1 = []
		self.queue2 = []

	def push(self, x):
		self.queue1.append(x)

	def pop(self):
		if len(self.queue2) != 0:
			return self.queue2.pop()
		else:
			while self.queue1:
				self.queue2.append(self.queue1.pop())
			return self.queue2.pop()

	def peek(self):
		if len(self.queue2) != 0:
			return self.queue2[-1]
		else:
			return self.queue1[0]

	def empty(self):
		if len(self.queue1) == 0 and len(self.queue2) == 0:
			return True
		return False