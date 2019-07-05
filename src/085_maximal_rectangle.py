"""
Given a 2D binary matrix filled with 0's and 1's, 
find the largest rectangle containing only 1's and return its area.

Input:
[
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]
Output: 6
"""

class Solution(object):

	# histogram solution
	def maxRectangle(self, matrix):
		if not matrix:
			return 0
		n = len(matrix[0])
		height = [0] * (n+1)
		res = 0
		for row in matrix:
			for i in range(n):
				height[i] = height[i] + 1 if row[i] == '1' else 0
			stack = [-1]

			for i in range(n+1):
				while height[i] < height[stack[-1]]:
					h = height[stack.pop()]
					w = i - 1 - stack[-1]
					res = max(res, h*w)
				stack.append(i)
		return res


	# DP algo
	def maxRectangle_2(self, matrix):
		if not matrix:
			return 0
		r, c = len(matrix), len(matrix[0])
		




test=[['1','0','1','0','0'],['1','0','1','1','1'],['1','1','1','1','1'],['1','0','0','1','0']]
A=Solution()
res=A.maxRectangle(test)
print(res)