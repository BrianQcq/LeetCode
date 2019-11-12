
class Solution(object):

	def findUnsortedSubarray(self, nums):
		ref = sorted(nums)
		for i in range(len(nums)):
			if nums[i] != ref[i]:
				break
		else:
			return 0

		for j in range(len(nums)-1, -1, -1):
			if nums[j] != ref[j]:
				break
		return j - i + 1

	def twopass(self, nums):
		l, r = 0, len(nums)-1
		max_, min_ = -float('inf'), float('inf')
		while l < r and nums[l] <= nums[l+1]:
			l += 1
		if l >= r:
			return 0

		while nums[r] >= nums[r-1]:
			r -= 1
		for i in range(l, r+1):
			min_ = min(min_. nums[i])
			max_ = max(max_, nums[i])

		while l >= 0 and nums[l] > min_:
			l -= 1
		while r < len(nums) and nums[r] < max_:
			r += 1
		return r - l - 1