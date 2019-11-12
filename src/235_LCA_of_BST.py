
class Solution(object):

	def LCA(self, root, p, q):
		node_val = root.val
		p_val = p.val
		q_val = q.val
		if p_val > node_val and q_val > node_val:
			return self.LCA(root.right, p, q)
		elif p_val < node_val and q_val < node_val:
			return self.LCA(root.left, p, q)
		else:
			return root