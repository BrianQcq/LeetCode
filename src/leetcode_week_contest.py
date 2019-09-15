# (u(love)i) --> ilioveu


class Solution(object):

	def reverse_parenthesis(self, s):
		stack = []
		for i in range(len(s)):
			if s[i] != ')':
				stack.append(s[i])
			else:
				temp=[]
				while stack[-1] != '(':
					temp.append(stack.pop())

				stack.pop()
				stack += temp
		return ''.join(stack)


A=Solution()
res=A.reverse_parenthesis('(u(lo(abc)ve)i)')
print(res)