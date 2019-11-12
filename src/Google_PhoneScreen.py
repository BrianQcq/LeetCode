# 1. Min Number of chiars
# (meeting room)

class MinNumofChair(object):

	def minNum(self, S, E):
		S = sorted(S)
		E = sorted(E)
		s, e = 0, 0
		room = avil = 0

		while s < len(S):
			if S[s] < E[e]:
				if avil == 0:
					room += 1
				else:
					avil -= 1
				s += 1
			else:
				avil += 1
				e += 1
		return room

# test=MinNumofChair()
# res=test.minNum([1, 2, 6, 5, 3], [5, 5, 7, 6, 8])
# print(res)


# 1. Overlap Picture



# 2. 给一张卡片，用5x5的grid表示，然后规定每行数字里的范围，并且每行数字都不能有重复。



# 3. 进程之间不能有conflict 问一个新进程能不能被加进机器, meeting rooms那一类的题



# 4. 


def addTwoNumbers(self, l1, l2):
	carry = 0
	root = n = ListNode(0)
	while l1 or l2:
		v1, v2 = 0
		if l1:
			v1 = l1.val
			l1 = l1.next
		if l2:
			v2 = l2.val
			l2 = l2.next
		carry, val = divmod(v1+v2+carry, 10)
		n.next = ListNode(val)
		n = n.next
	return root.next


class Solution(object):

	def longestPali(self, s):
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
		if len(s) == 0:
			return ''
		while l >= 0 and r < len(s) and s[l] == s[r]:
			l -= 1
			r += 1
		return s[l+1:r]


def lenOfLongestSubstring(s):
	visited = {}
	start = max_len = 0
	for i, ch in enumerate(s):
		if ch in visited and start <= visited[ch]:
			start = visited[ch] + 1
		else:
			max_len = max(max_len, i-start+1)
		visited[ch] = i
	return max_len


def reverseInt(x):
	if x >= 2**31 or x < -(2**31):
		return 0
	sign = 1
	if x < 0:
		sign = -1

	temp = str(sign * x)[::-1]
	res = sign * int(temp)
	if res >= 2**31 or res < -(2**31):
		return 0
	return res


def isNumPalin(x):
	if x < 0:
		return False
	num, res = x, 0
	while num:
		res = res * 10 + num%10
		num //= 10
	return res == x


def removeNthFromEnd(head, n):
	if not head:
		return None
	first = ListNode(0)
	first.next = head
	pos = cur = first
	for i in range(n):
		pos = pos.next
	while pos.next:
		cur = cur.next
		pos = pos.next
	cur.next = cur.next.next
	return first.next


def maxSubarraySum(nums):
	for i in range(1,len(nums)):
		if nums[i-1] > 0:
			nums[i] += nums[i-1]
	return max(nums)


def genSpiral(n):
	res = [[0] * n for i in range(n)]
	i, j, di, dj = 0, 0, 0, 1
	for k in range(n**2):
		res[i][j] = k+1
		if res[(i+di)%n][(j+dj)%n]:
			di, dj = dj, -di
		i += di
		j += dj
	return res


def stairs(n):
	if n == 1:
		return 1
	if n == 2:
		return 2
	return stairs(n-1) + stairs(n-2)


def genSubsets(nums):
	res = [[]]
	for num in nums:
		print(res)
		res += [i+[num] for i in res]
	return res


