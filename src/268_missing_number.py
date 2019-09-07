
class Solution(object):

	def missingNum(self, nums):
		temp = [i for i in range(len(nums)+1)]
		return sum(temp) - sum(nums)

	def missingNum_2(self, nums):
		ref = range(len(nums)+1)
		for i in nums:
			ref[i] = 0
		return max(ref)