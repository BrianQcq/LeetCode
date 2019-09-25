
class Solution(object):
	def subset(self, nums):

		res = [[]]
		for num in nums:
			res += [i + [num] for i in res]
			#print(res)
		return res

A=Solution()
res=A.subset([1,2,3])
#print(res)


# DFS
class Sol(object):

	def subset(self, nums):
		res = []
		self.dfs(nums, 0, [], res)
		return res

	def dfs(self, nums, idx, path, res):
		res.append(path)
		for i in range(idx, len(nums)):
			self.dfs(nums, i+1, path+[nums[i]], res)

B=Sol()
temp=B.subset([1,2,3])
print(temp)