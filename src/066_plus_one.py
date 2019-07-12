
class Solution(object):

	# using string
	def plusOne(self, digits):
		temp = ''
		for digit in digits:
			temp += str(digit)
		num = int(temp) + 1
		out = []
		for digit in str(num):
			out.append(int(digit))
		return out


	# improved version
	def plusOne_2(self, digits):
		num = 0
		for i in range(len(digits)):
			num = num * 10 + digits[i]
		return [int(i) for i in str(num+1)]

A=Solution()
res=A.plusOne_2([1,0,1,0,9,9,9])
print(res)