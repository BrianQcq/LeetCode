
class Solution(object):

	def partition(self, s):
		last = {char: i for i, char in enumerate(s)}
		res = []
		j = anchor = 0
		for i, c in enumerate(s):
			j = max(j, last[c])
			if i == j:
				res.append(i - anchor + 1)
				anchor = i + 1
		return res

A=Solution()
res=A.partition("ababcbacadefegdehijhklij")
print(res)