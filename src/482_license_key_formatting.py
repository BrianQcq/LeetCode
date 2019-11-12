
class Solution(object):

	def formatting(self, S, K):
		S = S.replace('-', '').upper()[::-1]
		return '-'.join(S[i:i+K] for i in range(0, len(S), K))[::-1]

A=Solution()
res=A.formatting("5F3Z-2e-9-w", 4)
print(res)