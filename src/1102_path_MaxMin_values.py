from heapq import *

class Solution(object):

	def maxMinPath(self, A):
		directions = [(1,0),(0,1),(-1,0),(0,-1)]
		r, c = len(A), len(A[0])
		ref = [[1 for i in range(c)] for j in range(r)]
		q = [(-A[0][0], 0, 0)]
		while q:
			res, x, y = heappop(q)
			if x == r - 1 and y == c - 1:
				return -res
			for d in directions:
				nx = x + d[0]
				ny = y + d[1]
				if 0 <= nx < r and 0 <= ny < c and ref[nx][ny]:
					heappush(q, (max(res, -A[nx][ny]), nx, ny))