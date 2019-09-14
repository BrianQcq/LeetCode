
class Solution(object):
	def flower(self, n):
		res = []
		if n == 1:
			return [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

		for num in range(10**(n-1), 10**n - 1):
			str_num = str(num)
			sum_ = 0
			for i in str_num:
				sum_ += int(i)**n
			if sum_ == num:
				res.append(num)
		return res

A=Solution()
res=A.flower(1)
print(res)