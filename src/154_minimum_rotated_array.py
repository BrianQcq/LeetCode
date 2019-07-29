
class Solution(object):

	def findMin(self, nums):
		l, r = 0, len(nums)-1
		while l < r:
			mid = (l+r)//2
			if nums[mid] > nums[r]:
				l = mid + 1
			elif nums[mid] < nums[l]:
				r = mid
			else:
				if(nums[r-1] > nums[r]):
					l = r
					break
				r -= 1
		print(l,r)
		return l

A=Solution()
res=A.findMin([1,3,5])
print(res)