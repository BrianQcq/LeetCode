"""
Given a sorted array nums, 
remove the duplicates in-place such that each element appear only once and return the new length.

Do not allocate extra space for another array, 
you must do this by modifying the input array in-place with O(1) extra memory.

"""

class Solution(object):
	def removeDupe(self, nums):
		if not nums:
			return 0

		newTail = 0
		for i in range(1, len(nums)):
			if nums[newTail] != nums[i]:
				newTail += 1
				nums[newTail] = nums[i]
		return nums[:newTail+1]

A=Solution()
res=A.removeDupe([0,0,0,1,2,2,3,3,4,5,7,7,8])
print(res)