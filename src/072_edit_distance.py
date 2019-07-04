"""
Given two words word1 and word2, find the minimum number of operations required to convert word1 to word2.

You have the following 3 operations permitted on a word:
Insert a character
Delete a character
Replace a character

Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')

Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation: 
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')
"""

class Solution(object):

	# recursion tle problem
	def minDist(self, word1, word2):
		# base case
		if not word1 and not word2:
			return 0
		if not word1:
			return len(word2)
		if not word2:
			return len(word1)

		# recursion case
		if word1[0] == word2[0]:
			return self.minDist(word1[1:], word2[1:])
		insert = 1 + self.minDist(word1, word2[1:])
		delete = 1 + self.minDist(word1[1:], word2)
		replace = 1 + self.minDist(word1[1:], word2[1:])
		return min(insert, delete, replace)

	# DP algo
	def minDist_2(self, word1, word2):
		m = len(word1)
		n = len(word2)
		dp = [[0 for x in range(n+1)] for x in range(m+1)]
		#dp = [[0] * (n+1)] * (m+1)

		for i in range(m+1):
			dp[i][0] = i
		for i in range(n+1):
			dp[0][i] = i

		for i in range(1, m+1):
			for j in range(1, n+1):
				if word1[i-1] == word2[j-1]:
					dp[i][j] = dp[i-1][j-1]
				else:
					dp[i][j] = 1 + min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1])
			#print(dp)
		return dp[-1][-1]

A=Solution()
out=A.minDist_2('intention','execution')
print(out)