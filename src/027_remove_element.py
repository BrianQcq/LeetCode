"""
Given an array nums and a value val, remove all instances of that value in-place and return the new length.

Do not allocate extra space for another array, 
you must do this by modifying the input array in-place with O(1) extra memory.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.
"""

class Solution(object):
	def removeElement(self, nums, val):
		if not nums:
			return 0

		tail = 0
		for i in range(len(nums)):
			if nums[i] != val:
				nums[tail] = nums[i]
				tail += 1
		return nums[:tail]

A=Solution()
res=A.removeElement([2,3,4,1,2,4,4,4,2,2,43,5,65,3,2], 2)
print(res)