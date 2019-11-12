class LongestPalin(object):

    def findlongest(self, s):
        res = ''
        for i in range(len(s)):
            temp = self.helper(s, i, i)
            if len(temp) > len(res):
                res = temp

            temp = self.helper(s, i, i+1)
            if len(temp) > len(res):
                res = temp
        return res

    def helper(self, s, l, r):
        if not s:
            return ''
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l+1:r]
A=LongestPalin()
res=A.findlongest('bccba')
print(res)


class ReverseLinkedList(object):

    def reverse(self, head):
        if not head:
            return None
        prev, cur = None, head
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        return prev