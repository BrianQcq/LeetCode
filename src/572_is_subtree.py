
class Solution(object):
	def isMatch(self, s, t):
		if not (s and t):
			return s == t
		return s.val == t.val and self.isMatch(s.left, t.left) and self.isMatch(s.right, t.right)

	def isSubtree(self, s, t):
		if not s:
			return False
		if self.isMatch(s, t):
			return True
		return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)