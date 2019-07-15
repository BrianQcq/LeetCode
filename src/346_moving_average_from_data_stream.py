
class Solution(object):

	def __init__(self, size):
		self.queue = []
		self.i = 0
		self.summ = 0
		self.size = size

	def next(self, val):
		self.queue.append(val)
		self.i += 1
		self.summ += val
		if self.i <= self.size:
			return float(self.summ) / float(self.i)
		else:
			self.summ -= self.queue[self.i - self.size - 1]
			self.i -= 1
			return float(self.summ) / float(self.size)