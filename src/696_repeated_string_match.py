
class Solution(object):

	def repeatedMatch(self, A, B):
		count = 0
		temp = ''
		while len(temp) < len(B):
			temp += A
			count += 1
			if B in temp:
				return count
		temp += A
		count += 1
		return count if B in temp else -1

A=Solution()
res=A.repeatedMatch('abcd', 'bcdabcdabcdabcda')
print(res)