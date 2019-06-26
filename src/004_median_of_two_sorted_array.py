"""
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

nums1 = [1, 3]
nums2 = [2]

The median is 2.0

nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
"""

class Solution(object):
	def findMedian(self, nums1, nums2):
		l = len(nums1) + len(nums2)
		if l % 2 == 1:
			return self.find_k_th(nums1, nums2, l//2)
		else:
			return (self.find_k_th(nums1, nums2, l//2) + self.find_k_th(nums1, nums2, l//2 - 1)) / 2


	def find_k_th(self, A, B, k):
		if not A:
			return B[k]
		if not B:
			return A[k]

		m = len(A) // 2
		n = len(B) // 2
		med_A = A[m]
		med_B = B[n]

		if m + n < k:
			if med_A > med_B:
				return self.find_k_th(A, B[n+1:], k - n -1)
			else:
				return self.find_k_th(A[m+1:], B, k - m -1)
		else:
			if med_A > med_B:
				return self.find_k_th(A[:m], B, k)
			else:
				return self.find_k_th(A, B[:n], k)


A=Solution()
res=A.findMedian([3,4,5,6,7,8],[5,6,7,8,9,10])
print(res)