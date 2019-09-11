
class Solution(object):

	# TLE O(n^2) time comp
	def findDisNum(self, nums):
		ref = [i+1 for i in range(len(nums))]
		temp = list(set(nums))
		return [i for i in ref if i not in temp]



	def findDisNum(self, nums):
		for i in range(len(nums)):
			idx = abs(nums[i]) - 1
			nums[idx] = -abs(nums[idx])
		return [i+1 for i in range(len(nums)) if nums[i] > 0]

	def findDisNum(self, nums):
		return list(set(range(1, len(nums)+1)) - set(nums))