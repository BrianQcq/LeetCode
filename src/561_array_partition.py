

class Solution(object):
	def arrayPairSum(self, nums):
		l = len(nums)
		nums.sort()
		idx, out = 0, 0
		while idx < l:
			out += nums[idx]
			idx += 2
		return out