# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque

class Solution(object):

	def distanceK(self, root, target, k):

		def dfs(node):
			if not node:
				return
			if node.left:
				parent[node.left] = node
				dfs(node.left)
			if node.right:
				parent[node.right] = node
				dfs(node.right)

		parent = {root:None}
		dfs(root)
		visited = {target}
		q = deque([(target, 0)])
		while q:
			if q[0][1] == k:
				return [node.val for node, dis in q]
			node. dis = q.popleft()
			for neighbor in [node.left, node.right, parent[node]]:
				if neighbor and neighbor not in visited:
					q.append(neighbor)
					visited.add(neighbor)
		return []