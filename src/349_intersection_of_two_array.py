
class Solution(object):

	# brute force
	def intersection(self, nums1, nums2):
		out = []
		for num in nums1:
			if num in nums2 and num not in out:
				out.append(num)
		return num

	# optimized time complexity
	def intersection_2(self, nums1, nums2):
		out = []
		nums2.sort()
		#print(nums2)
		for num in nums1:
			l, r = 0, len(nums2)-1
			while l <= r:
				mid = (l+r)//2
				if nums2[mid] == num and num not in out:
					out.append(num)
					break
				elif nums2[mid] > num:
					r = mid - 1
				else:
					l = mid + 1
		return out

A=Solution()
res=A.intersection_2([5,1,2,3,1],[2,2,1,5,3])
print(res)