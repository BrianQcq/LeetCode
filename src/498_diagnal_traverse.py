import collections

class Solution(object):

	def findDiagnalOrder(self, matrix):
		result = []
		dd = collections.defaultdict(list)
		if not matrix :
			return result

		for i in range(len(matrix)):
			for j in range(len(matrix[0])):
				dd[i+j].append(matrix[i][j])
		for i in range(len(matrix) + len(matrix[0]) - 1):
			if i % 2 == 0:
				result += dd[i][::-1]
			else:
				result += dd[i]
		return result

	def findDiagnalOrder



A=Solution()
res=A.findDiagnalOrder([[1,2,3],[4,5,6],[7,8,9]])
print(res)