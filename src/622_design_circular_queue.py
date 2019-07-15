
class MyCircularQueue(object):

	def __init__(self, k):
		self.size = 0
		self.max_size = k
		self.front = self.rear = -1
		self.queue = [0] * k

	def enQueue(self, value):
		if self.isFull():
			return False
		else:
			if self.rear == -1:
				self.rear = self.front = 0
			else:
				self.rear = (self.rear + 1) % self.max_size
			self.queue[self.rear] = value
			self.size += 1
			return True

	def deQueue(self):
		if self.isEmpty():
			return False
		else:
			if self.front == self.rear:
				self.front = self.rear = -1
			else:
				self.front = (self.front + 1) % self.max_size
			self.size -= 1
			return True

	def Front(self):
		return self.queue[self.front] if self.size else -1

	def Rear(self):
		return self.queue[self.rear] if self.size else -1

	def isEmpty(self):
		return self.size == 0

	def isFull(self):
		return self.size == self.max_size
