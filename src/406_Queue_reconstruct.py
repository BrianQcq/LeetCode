
class Solution(object):

	def reconstruct(self, people):
		res = []
		people.sort(key = lambda x: (-x[0], x[1]))
		for p in people:
			res.insert(p[1], p)
		return res