from collections import deque

class Solution(object):

	def maxLevelSum(self, root):
		maxsum, level, maxlevel = -float('inf'), 0, 0
		q = deque()
		q.append(root)
		while q:
			level += 1
			tempsum = 0
			for i in range(len(q)):
				node = q.popleft()
				tempsum += node.val
				if node.left:
					q.append(node.left)
				if node.right:
					q.append(node.right)
			if tempsum > maxsum:
				maxsum, maxlevel = tempsum, level
		return maxlevel