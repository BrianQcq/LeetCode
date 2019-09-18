from collections import deque

class Solution(object):

	def __init__(self):
		self.stack = deque()

	def push(self, x):
		q = self.stack
		q.append(x)
		for i in range(len(q)-1):
			q.append(q.popleft())

	def pop(self):
		return self.stack.popleft()

	def top(self):
		return self.stack[0]

	def empty(self):
		return len(self.stack) == 0