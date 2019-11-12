
class Solution(object):

	def rob(self, nums):

		def simple_rob(nums):
			prev, now = 0, 0
			for num in nums:
				prev, now = now, max(num+prev, now)
			return now

		if not nums:
			return 0
		if len(nums) == 1:
			return nums[0]
		return max(simple_rob(nums[1:]), simple_rob(nums[:-1]))