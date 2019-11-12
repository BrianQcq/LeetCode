
class Solution(object):

	def findJudge(self, N, trust):
		trusted = [0] * (N+1)
		for i,j in trust:
			trusted[i] -= 1
			trusted[j] += 1

		for i in range(1, len(trusted)):
			if trusted[i] == N - 1:
				return i
		return -1