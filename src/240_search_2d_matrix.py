



























class Solution(object):

	def searchMatrix(self, matrix, target):
		for row in matrix:
			if target in row:
				return True
		return False

	def searchMatrix_2(self, matrix, target):
		if not matrix or not matrix[0]:
			return False

		row, col, width = len(matrix)-1, 0, len(matrix[0])
		while row >= 0 amd col < width:
			if matrix[row][col] == target:
				return True
			elif matrix[row][col] > target:
				row -= 1
			else:
				col += 1
		return False
