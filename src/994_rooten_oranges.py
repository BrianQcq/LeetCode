from collections import deque

class Solution(object):

	def orangeRotting(self, grid):
		r, c = len(grid), len(grid[0])
		q = deque([])
		cnt = 0
		for i in range(r):
			for j in range(c):
				if grid[i][j] == 1:
					cnt += 1
				if grid[i][j] == 2:
					q.append((i,j))
		res = 0
		while q:
			for _ in range(len(q)):
				i, j = q.popleft()
				for x, y in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]:
					if 0 <= x < r and 0 <= y < c and grid[x][y] == 1:
						grid[x][y] = 2
						cnt -= 1
						q.append((x,y))
			res += 1
		return max(0, res-1) if cnt == 0 else -1