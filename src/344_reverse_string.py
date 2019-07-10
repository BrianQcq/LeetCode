
class Solution(object):
	def reverseString(self, s):
		l = len(s)
		if l < 2:
			return s
		return self.reverseString(s[l//2:]) + self.reverseString(s[:l//2])

	def reverseString_2(self, s):
		l, r = 0, len(s)-1
		while l <= r:
			s[l], s[r] = s[r], s[l]
			l += 1; r -= 1


A=Solution()
res=A.reverseString_2(['h','e','l','l','0'])
print(res)