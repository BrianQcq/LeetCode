
class Solution(object):

	def detectCycle(self, head):
		if not head or not head.next:
			return None
		slow = head
		fast = head
		hasCycle = False
		while fast.next and fast.next.next:
			slow = slow.next
			fast = fast.next.next
			if slow is fast:
				hasCycle = True
				break

		if not hasCycle:
			return None
		slow = head
		while slow is not fast:
			slow = slow.next
			fast = fast.next
		return slow