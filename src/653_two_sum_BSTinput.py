# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

	def findTarget(self, root, k):
		nums, stack = [], []
		while True:
			while root:
				stack.append(root)
				root = root.left
			if not stack:
				break
			node = stack.pop()
			nums.append(node.val)
			root = node.right

		l, r = 0, len(nums)-1
		while l < r:
			if nums[l] + nums[r] == k:
				return True
			elif nums[l] + nums[r] > k:
				r -= 1
			else:
				l += 1
		return False