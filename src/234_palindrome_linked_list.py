
class Solution(object):

	# recursive but tle
	def isPalindrome(self, head):
		if not head or not head.next:
			return True
		tail = head
		while tail.next.next:
			tail = tail.next
		if head.val == tail.next.val:
			tail.next = None
			head = head.next
			return self.isPalindrome(head)
		else:
			return False


	# reverse the second half
	def isPalindrome_2(self, head):
		if not head or not head.next:
			return True
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        node = None
        while slow:
            nxt = slow.next
            slow.next = node
            node = slow
            slow = nxt
        while node:
            if node.val != head.val:
                return False
            else:
                node = node.next
                head = head.next
        return True