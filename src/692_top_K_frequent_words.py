from heapq import *
from collections import Counter

class Solution(object):

	def topKFrequent(self, words, k):
		counts = Counter(words)
		heap = [(-val, key) for key, val in counts.items()]
		heapify(heap)
		return [heappop(heap)[-1] for _ in range(k)]