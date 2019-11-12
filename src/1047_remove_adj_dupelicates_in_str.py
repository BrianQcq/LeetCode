
class Solution(object):

	# naive
	def remove(self, s):
		i = self.hasDupe(s)
		while i is not False:
			s = s[:i] + s[i+2:]
			i = self.hasDupe(s)
		return s

	def hasDupe(self, s):
		for i in range(len(s)-1):
			if s[i] == s[i+1]:
				return i
			return False


class Solution_2(object):

	# O(N) time
	def remove(self, s):
		stack = ['#']
		for char in s:
			stack.append(char)
			if stack[-1] == stack[-2]:
				stack.pop()
				stack.pop()
		return ''.join(stack[1:])