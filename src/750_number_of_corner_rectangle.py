
class Solution(object):

	# brute force
	def numRectangle(self, grid):
		if not grid or not grid[0]:
			return 0
		r, c = len(grid), len(grid[0])
		res = 0
		for i in range(r-1):
			for j in range(i+1, r):
				count = 0
				for k in range(c):
					if grid[i][k] and grid[j][k]:
						res += count
						count += 1
		return res

	# DP algo
	def numRectangle_2(self, grid):
		if not grid or not grid[0]:
			return 0
		r, c = len(grid), len(grid[0])
		dp = [[0 for x in range(c)] for x in range(r)]
		res = 0
		#dp = [[0]*c for x in range(r)]
		#print(dp)
		for i in range(r):
			for j in range(c):
				if grid[i][j] == 0:
					continue
				for k in range(j+1, c):
					if grid[i][k] == 0:
						continue
					res += dp[j][k]
					dp[j][k] += 1
		return res

	# using set
	def numRectangle_3(self, grid):
		if not grid or not grid[0]:
			return 0
		r, c = len(grid), len(grid[0])
		dp_set = []
		res = 0
		for i in range(r):
			dp_set.append(set(idx for idx, val in enumerate(grid[i]) if val))
			for prev in range(i):
				matches = len(dp_set[i] & dp_set[prev])
				if matches >= 2:
					res += matches * (matches - 1) // 2
		return res


A=Solution()
res=A.numRectangle_3([[1,1,1],[1,1,1],[1,1,1]])
print(res)