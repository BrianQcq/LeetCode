
class Solution(object):

	def generate(self, n):
		if not n:
			return []
		left, right, res = n, n, []
		self.dfs(left, right, res, '')
		return res

	def dfs(self, l, r, res, strs):
		if r < l:
			return
		if not l and not r:
			res.append(strs)
			return
		if l:
			self.dfs(l-1, r, res, strs+'(')
		if r:
			self.dfs(l, r-1, res, strs+')')