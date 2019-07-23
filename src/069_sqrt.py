
class Solution(object):

	# Newton's method
	def mySqrt(self, x):
		res = x
		while res**2 > x:
			res = (res + x//res)//2
		return res

	# Binray Search
	def mySqrt_2(self, x):
		ans = 0
		l, r = 1, x
		while l <= r:
			mid = (l + r)//2
			if mid <= x//mid:
				l = mid + 1
				ans = mid
			else:
				r = mid - 1
		return ans



A=Solution()
res=A.mySqrt_2()
print(res)