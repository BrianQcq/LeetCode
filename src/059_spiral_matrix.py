
class Solution(object):

	def generate(self, n):
		A = [[0] * n for _ in range(n)]
		i, j, di, dj = 0, 0, 0, 1
		for k in range(n*n):
			A[i][j] = k + 1
			if A[(i+di)%n][(j+dj)%n]:
				di, dj = dj, -di
			i += di
			j += dj
		return A

A=Solution()
res=A.generate(5)
print(res)