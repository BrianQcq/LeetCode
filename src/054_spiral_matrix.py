import collections

class Solution(object):

	# very good solution from discussion
	def spiral(self, matrix):
		return matrix and [*matrix.pop(0)] + self.spiral([*zip(*matrix)][::-1])

	# mutating the matrix
	def spiral_2(self, matrix):
		result = []
		while matrix:
			result += matrix.pop(0)  # take the first row
			if matrix and matrix[0]: # take the right column
				for row in matrix:
					result.append(row.pop())
			if matrix:				 # take the bottom row in reverse
				result += matrix.pop()[::-1]
			if matrix and matrix[0]: # take the left column in reverse
				for row in matrix[::1]:
					result.append(row.pop(0))
		return result


A=Solution()
res=A.spiral([[1,2,3],[4,5,6],[7,8,9]])
print(res)