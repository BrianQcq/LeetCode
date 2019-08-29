
class Solution(object):

	def pathSum(self, root, sum):
		if not root:
			return 0
		path_root = self.count(root, sum)
		path_left = self.pathSum(root.left, sum)
		path_right = self.pathSum(root.right, sum)
		return path_root + path_left + path_right

	def count(self, node, sum):
		if not node:
			return 0
		isMe = 1 if node.val == sum else 0
		left = self.count(node.left, sum - node.val)
		right = self.count(node.right, sum - node.val)
		return isMe + left + right