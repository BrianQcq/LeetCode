class Solution(object):

	def merge_sort(self, nums):
		
		def merge(A, B):
			C = []
			while A and B:
				C.append(A.pop(0)) if A[0] < B[0] else C.append(B.pop(0))
			return C + (A or B)

		n = len(nums)
		return nums if n < 2 else merge(self.merge_sort(nums[:n>>1]), self.merge_sort(nums[n>>1:]))

A=Solution()
res=A.merge_sort([3,4,6,2,3,4,1,3,5,6,7])		
print(res)

class Sol(object):

	def merge_sort(self, nums):
		if len(nums) <= 1:
			return nums

		pivot = len(nums) // 2
		left = self.merge_sort(nums[:pivot])
		right = self.merge_sort(nums[pivot:])
		return self.merge(left, right)

	def merge(self, A, B):
		C = []
		while A and B:
			C.append(A.pop(0)) if A[0] < B[0] else C.append(B.pop(0))
		return C + (A or B)

B=Sol()
res2=B.merge_sort([1,3,4,2,5])
print(res2)