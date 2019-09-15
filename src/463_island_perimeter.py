
class Solution(object):

	def getPerimeter(self, grid):
		if not grid:
			return 0
		island = neighbor = 0
		for i in range(len(grid)):
			for j in range(len(grid[0])):
				if grid[i][j] == 1:
					island += 1
					if i < len(grid)-1 and grid[i+1][j] == 1:
						neighbor += 1
					if j < len(grid[0])-1 and grid[i][j+1] == 1:
						neighbor += 1
		return 4 * island - 2 * neighbor

A=Solution()
res=A.getPerimeter([[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]])
print(res)