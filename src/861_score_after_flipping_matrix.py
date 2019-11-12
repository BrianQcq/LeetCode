
class Solution(object):

	def matrixScore(self, A):
		r, c = len(A), len(A[0])
		res = r * 2**(c-1)
		for j in range(1, c):
			cur = sum(A[i][j] == A[i][0] for i in range(r))
			res += max(cur, r - cur) * 2**(c-1-j)
		return res


A=Solution()
res=A.matrixScore([[0,0,1,1],[1,0,1,0],[1,1,0,0]])
print(res)