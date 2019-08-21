
class Solution(object):

	def preorder(self, root):
		if not root:
			return []
		stack = [root]
		res = []
		while stack:
			r = stack.pop()
			if r is not None:
				res.append(r.val)
				if r.right is not None:
					stack.append(r.right)
				if r.left is not None:
					stack.append(r.left)

		return res