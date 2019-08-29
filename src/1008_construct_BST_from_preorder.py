
class Solution(object):

	# recursion algo
	def bstFromPreorder(self, preorder):
		if not preorder:
			return None
		root = TreeNode(preorder[0])
		if len(preorder) == 1:
			return root
		idx = 1
		while idx < len(preorder) and preorder[idx] < root.val:
			idx += 1
		root.left = self.bstFromPreorder(preorder[1:idx])
		root.right = self.bstFromPreorder(preorder[idx:])
		return root

	# stack 
	def bstFromPreorder_2(self, preorder):
		root = TreeNode(preorder[0])
		stack = [root]
		for value in preorder[1:]:
			if value < stack[-1].val:
				stack[-1].left = TreeNode(value)
				stack.append(stack[-1].left)
			else:
				while stack and stack[-1].val < value:
					last = stack.pop()
				last.right = TreeNode(value)
				stack.append(last.right)
		return root