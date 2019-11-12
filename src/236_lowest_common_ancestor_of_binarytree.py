
class Solution(object):

	def LCA(self, root, p, q):
		stack = [root]
		ref = {root: None}
		while q not in ref or p not in ref:
			node = stack.pop()
			if node.left:
				ref[node.left] = node
				stack.append(node.left)
			if node.right:
				ref[node.right] = node
				stack.append(node.right)

		ancestor = set()
		while q:
			ancestor.add(q)
			q = ref[q]
		while p not in ancestor:
			p = ref[p]
		return p

	def LCA_2(self, root, p, q):
		if not root:
			return None
		if p == root or q == root:
			return root
		l = self.LCA_2(root.left, p, q)
		r = self.LCA_2(root.right, p, q)
		if l and r:
			return root
		if not l:
			return r
		if not r:
			return l