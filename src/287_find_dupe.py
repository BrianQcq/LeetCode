
class Solution(object):

	def findDupe(self, nums):

		nums.sort()
		prev = nums[0]
		for i in range(1, len(nums)):
			if nums[i] != prev:
				prev = nums[i]
			else:
				return prev

A=Solution()
res=A.findDupe([3,1,3,2,4,5])
print(res)