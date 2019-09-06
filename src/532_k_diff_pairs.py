
class Solution(object):

	def findPairs(self, nums, k):
		nums.sort()
		count = []
		ref = {}
		for i in range(len(nums)):
			if nums[i] in ref:
				count.append((ref[nums[i]], nums[i]))
			ref[nums[i] + k] = nums[i]
		print(count)
		return 


A=Solution()
res=A.findPairs([1,3,1,5,4], 0)
print(res)