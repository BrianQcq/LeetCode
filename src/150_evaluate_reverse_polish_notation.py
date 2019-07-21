import operator	

class Solution(object):

	def evalRPN(self, tokens):

		ops = {"+": operator.add, "-": operator.sub, '/': operator.floordiv, "*": operator.mul}
		stack = []

		for item in tokens:
			stack.append(item)
			if stack[-1] in ops.keys():
				temp1 = int(stack.pop(-3))
				temp2 = int(stack.pop(-2))
				if stack[-1] == "/" and temp1*temp2 < 0 and temp1%temp2 != 0:
					val = ops[stack.pop()](temp1, temp2) + 1
				else:
					val = ops[stack.pop()](temp1, temp2)
				stack.append(val)
		return stack[0]
		# Need to think about the minus division case, e.g. -> -1/22 should be 0 instead of -1 in python

A=Solution()
res=A.evalRPN(["4","-2","/","2","-3","-","-"])
print(res)