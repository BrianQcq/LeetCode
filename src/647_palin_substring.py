
class Solution(object):

	def countSubstring(self, s):

		def check(s):
			return s == s[::-1]

		count = 0
		for i in range(len(s)):
			for j in range(i+1:len(s)+1):
				if check(s[i:j]):
					count += 1
		return count


	def countSubstring_2(self, s):

		res = 0
		for center in range(2*len(s) - 1):
			left = center // 2
			right = left + center % 2
			while left >= 0 and right < len(s) and s[left] == s[right]:
				res += 1
				left -= 1
				right += 1
		return res
