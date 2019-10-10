
# DFS solution

class Solution(object):

	def numIsland(self, grid):
		if not grid or not grid[0]:
			return 0
		count = 0
		for i in range(len(grid)):
			for j in range(len(grid[0])):
				if grid[i][j] == '1':
					self.dfs(grid, i, j)
					count += 1
		return count


	def dfs(self, grid, i, j):
		if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != '1':
			return
		grid[i][j] = '#'
		self.dfs(grid, i+1, j)
		self.dfs(grid, i-1, j)
		self.dfs(grid, i, j+1)
		self.dfs(grid, i, j-1)

A=Solution()
res=A.numIsland([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]])
print(res)


# BFS solution
from collections import deque	

class Solution_BFS(object):

	def numIslands(self, grid):
		if not grid or not grid[0]:
			return 0
		r, c = len(grid), len(grid[0])
		count = 0
		for i in range(r):
			for j in range(c):
				if grid[i][j] == '1':
					grid[i][j] = '0'
					count += 1
					queue = deque([(i-1,j),(i+1,j),(i,j-1),(i,j+1)])
					while queue:
						#print(queue)
						x,y = queue.popleft()
						if x < 0 or x >= r or y < 0 or y >= c:
							continue
						else:
							if grid[x][y] == '0':
								continue
							else:
								grid[x][y] = '0'
								queue.extend([(x-1,y),(x+1,y),(x,y-1),(x,y+1)])
		return count

B=Solution_BFS()
res_B = B.numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]])
print(res_B)