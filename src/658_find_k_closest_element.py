
class Solution(object):
	def findKClosest(self, arr, k, x):
		l, r = 0, len(arr)-k
		while l < r:
			mid = (l + r)//2
			if x - arr[mid] > arr[mid+k] - x:
				l = mid + 1
			else:
				r = mid
		print(l,r)
		print(mid)
		return arr[l:l+k]

A=Solution()
res=A.findKClosest([1,1,2,2,3,4,5,8,8,9], 3, 2)
print(res)