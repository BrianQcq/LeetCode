
class MinStack(object):

	def __init__(self):
		self.stack =[]
		self.size = 0

	def push(self, x):
		self.stack.append(x)
		self.size += 1

	def pop(self):
		if self.size == 0:
			return False
		self.stack.pop()

	def top(self):
		if self.size == 0:
			return False
		return self.stack[-1]

	def getMin(self):
		if self.size == 0:
			return False
		return min(self.stack)


# improved version
class MinStack_2(object):

	def __init__(self):
		self.stack = []
		self.size = 0

	def push(self, x):
		curMin = self.getMin()
		if x <= curMin:
			curMin = x
		self.stack.append((x, curMin))
		self.size += 1

	def pop(self):
		self.stack.pop()
		self.size -= 1

	def top(self):
		if self.size == 0:
			return False
		return self.stack[-1][0]

	def getMin(self):
		# to get the min for the first push
		if self.size == 0:
			return float('inf')
		return self.stack[-1][1]