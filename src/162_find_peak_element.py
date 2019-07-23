
class Solution(object):

	def findPeakElement(self, nums):

		l, r = 0, len(nums) - 1
		while l < r:
			mid = (l + r)//2
			if nums[mid] > nums[mid+1]:
				r = mid
			else:
				l = mid + 1
		return l


A=Solution()
res=A.findPeakElement([1,1,2,3,4,1,0,2,0])
print(res)