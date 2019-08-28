
class Solution(object):

	# recursive DFS
	def pathSum(self, root, sum):
		if not root:
			return []
		res = []
		self.dfs(root, sum, [], res)
		return res

	def dfs(self, root, sum, ls, res):
		if not root.left and not root.right and sum == root.val:
			ls.append(root.val)
			res.append(ls)
		if root.left:
			self.dfs(root.left, sum-root.val, ls + [root.val], res)
		if root.right:
			self.dfs(root.right, sum-root.val, ls + [root.val], res)

	# BFS with stack
	def pathSum_BFS(self, root, sum):
		if not root:
			return []
		res = []
		queue = [(root, root.val, [root.val])]
		while queue:
			curr, val, ls = queue.pop(0)
			if not curr.left and not curr.right and val == sum:
				res.append(ls)
			if curr.left:
				queue.append([curr.left, val + curr.left.val, ls + [curr.left.val]])
			if curr.right:
				queue.append([curr.right, val + curr.right.val, ls + [curr.right.val]])
		return res