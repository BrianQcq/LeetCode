
class Solution(object):

	def hasCycle(self, head):

		if not head or not head.next:
			return False
		slow = head
		fast = head
		while fast.next and fast.next.next:
			slow = slow.next
			fast = fast.next.next
			if slow is fast:
				return True
		return False