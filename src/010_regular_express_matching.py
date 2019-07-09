"""
'.' Matches any single character.
'*' Matches zero or more of the preceding element.

Input:
s = "aa"
p = "a"
Output: false

Input:
s = "aa"
p = "a*"
Output: true

Input:
s = "ab"
p = ".*"
Output: true

Input:
s = "aab"
p = "c*a*b"
Output: true

Input:
s = "mississippi"
p = "mis*is*p*."
Output: false
"""


class Solution(object):
	def isMatch(self, s, p):
		dp = [[False] * (len(p)+1) for _ in range(len(s) + 1)]
		dp[0][0]= True

		for i in range(1, len(p)+1):
			if p[i-1] == '*':
				dp[0][i] = dp[0][i-2]
		#for item in dp:
		#	print(item)
		for i in range(1, len(s)+1):
			for j in range(1, len(p)+1):
				if s[i-1] == p[j-1] or p[j-1] == '.':
					dp[i][j] = dp[i-1][j-1]
				elif p[j-1] == '*':
					dp[i][j] = dp[i][j-2]
					if s[i-1] == p[j-2] or p[j-2] == '.':
						dp[i][j] |= dp[i-1][j]
				else:
					dp[i][j] = False
		for item in dp:
			print(item)
		return dp[-1][-1]

A=Solution()
res=A.isMatch('aaa', 'ab*a*c*a')
print(res)