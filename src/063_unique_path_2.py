"""
Now consider if some obstacles are added to the grids. How many unique paths would there be?

An obstacle and empty space is marked as 1 and 0 respectively in the grid.

Input:
[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
Output: 2
Explanation:
There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right
"""

class Solution(object):
	def uniqupaths(self, obstacleGrid):
		self.convert(obstacleGrid)

		for i in range(1, len(obstacleGrid)):
			for j in range(1, len(obstacleGrid[0])):
				if obstacleGrid[i][j] == 0:
					continue
				obstacleGrid[i][j] = obstacleGrid[i-1][j] + obstacleGrid[i][j-1]
		return obstacleGrid[-1][-1]

	def convert(self, nums):
		for x in range(1,len(nums)):
			for y in range(1,len(nums[0])):
				if nums[x][y] == 1:
					nums[x][y] = 0
				else:
					nums[x][y] = 1
		#print(nums)
		for x in range(len(nums[0])):
			if x == 0:
				if nums[0][x] == 1:
					nums[0][x] = 0
				else:
					nums[0][x] = 1
			else:
				if nums[0][x] == 1:
					nums[0][x] = 0
				elif nums[0][x] == 0 and nums[0][x-1] == 0:
					continue
				else:
					nums[0][x] = 1

		for y in range(1, len(nums)):
			if nums[y][0] == 1:
				nums[y][0] = 0
			elif nums[y][0] == 0 and nums[y-1][0] == 0:
				continue
			else:
				nums[y][0] = 1

A=Solution()
res=A.uniqupaths([[0,0,0],[0,1,0],[0,0,0]])
print(res)