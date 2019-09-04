
class Solution(object):

	def fizzBuzz(self, n):

		res = []
		for i in range(n):
			if (i+1) % 5 == 0 and (i+1) % 3 == 0:
				res.append('FizzBuzz')
			elif (i+1) % 5 == 0:
				res.append('Buzz')
			elif (i+1) % 3 == 0:
				res.append('Fizz')
			else:
				res.append(str(i+1))
		return res

A=Solution()
res=A.fizzBuzz(20)
print(res)