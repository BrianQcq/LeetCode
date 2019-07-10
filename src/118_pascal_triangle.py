
class Solution(object):

	def generate(self, numRows):

		pascal = [[1]*(i+1) for i in range(numRows)]
		for i in range(2, numRows):
			for j in range(1,i):
				pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j]
		return pascal

	# optimize to O(n) space
	def generate_2(self, kthRows):

		pascal = [0] * (kthRows+1)
		pascal[0] = 1
		for i in range(1, len(pascal)):
			j = i
			while j >= 1:
				pascal[j] += pascal[j-1]
				j -= 1

		print(pascal)

A=Solution()
res=A.generate_2(4)
print(res)