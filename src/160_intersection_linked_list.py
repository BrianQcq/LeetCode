
class Solution(object):

	def getIntersectNode(self, headA, headB):
		if not headA or not headB:
			return None
		a = headA
		b = headB
		while a is not b:
			a = headB if a is None else a.next
			b = headA if b is None else b.next
		return a