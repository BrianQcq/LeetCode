
class Solution(object):

	def twoSumLessThanK(self, nums, k):
		nums.sort()
		res = -1
		l, r = 0, len(nums)-1
		while l < r:
			if nums[l] + nums[r] < k:
				res = max(res, nums[l]+nums[r])
				l += 1
			else:
				r -= 1
		return res