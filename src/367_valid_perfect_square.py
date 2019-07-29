
class Solution(object):

	def isPerfectSquare(self, num):
		l, r = 0, num
		while l <= r:
			mid = (l+r)//2
			#print(mid)
			if mid ** 2 == num:
				return True
			elif mid ** 2 > num:
				r = mid - 1
			else:
				l = mid + 1
		return False


	# Math Solution
	# any square numbe is 1 + 3 + 5 + 7 + ...
	def isPerfectSquare_2(self, num):
		i = 1
		while num > 0:
			num -= i
			i += 2
		return num == 0

A=Solution()
res=A.isPerfectSquare_2(16)
print(res)