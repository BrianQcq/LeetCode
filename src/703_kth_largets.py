from bisect import 
import heapq

# Binary search method, time comp: O(n * (n + logn))
class KthLargest(object):

	def __init__(self, k, nums):
		self.nums = sorted(nums)
		self.k = k

	def add(self, val):
		idx = bisect_left(self.nums, val)
		self.nums.insert(idx, val)
		return self.nums[-self.k]



class Sol(object):

	def __init__(self, k, nums):
		self.pool = nums
		self.k = k
		heapq.heapify(self.pool)
		while len(self.pool) > self.k:
			heapq.heappop(self.pool)

	def add(self, val):
		if len(self.pool) < self.k:
			heapq.heappush(self.pool, val)
		elif self.pool[0] < val:
			heapq.heapreplace(self.pool, val)
		return self.pool[0]