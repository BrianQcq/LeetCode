
class Solution(object):

	# time complexity O(n^2)
	def pivotIndex(self, nums):
		for i in range(len(nums)):
			if sum(nums[:i]) == sum(nums[i+1:]):
				return i
		return -1

	def pivotIndex_2(self, nums):
		total = sum(nums)
		temp = 0
		for i, item in enumerate(nums):
			if temp == total - temp - item:
				return i
			temp += item
		return -1


A=Solution()
res=A.pivotIndex_2([1,7,3,6,5,6])
print(res)