
class Solution(object):

	def tree2str(self, t):
		if not t:
			return ''

		res = str(t.val) + ''
		left = self.tree2str(t.left)
		right = self.tree2str(t.right)

		if not left and not right:
			return res
		if not left:
			return res + '()' + '(' + right + ')'
		if not right:
			return res + '(' + left + ')'
		return res + '(' + left + ')' + '(' + right + ')'
