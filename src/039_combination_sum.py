
class Solution(object):

	def combinationSum(self, candidates, target):
		res = []
		self.dfs(candidates, [], res, target)
		return res

	def dfs(self, nums, path, res, target):
		if target == 0:
			if sorted(path) not in res:
				res.append(sorted(path))
				return
		if target < 0:
			return
		for num in nums:
			self.dfs(nums, path+[num], res, target-num)