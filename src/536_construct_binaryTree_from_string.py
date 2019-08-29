
class Solution(object):

	def str2tree(self, s):
		if not s:
			return None
		stack = []
		string = ''
		for i in s:
			if i not in ['(', ')']:
				string += i
			else:
				if string:
					stack.append(TreeNode(int(string)))
					string = ''
				if i == ')':
					temp = stack.pop()
					if stack[-1].left:
						stack[-1].right = temp
					else:
						stack[-1].left = temp
		if string:
			stack.append(TreeNode(int(string)))
		return stack[-1]
