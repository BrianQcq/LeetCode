
class Solution(object):

	def getSum(self, a, b):
		MAX = 0x7FFFFFFF
		mask = 0xFFFFFFFF
		while b != 0:
			a, b = (a ^ b) & mask, ((a & b) << 1) & mask
		return a if a < MAX else ~(a ^ mask)

A=Solution()
res=A.getSum(5,-6)
print(res)