# 532. K-diff Pairs in an Array
# Input: [3, 1, 4, 1, 5], k = 2
# Output: 2
# Explanation: There are two 2-diff pairs in the array, (1, 3) and (3, 5).
# Although we have two 1s in the input, we should only return the number of unique pairs.

def findPairs(nums, k):
	nums.sort()
	count = []
	ref = {}
	for i in range(len(nums)):
		if nums[i] in ref:
			count.append((ref[nums[i]],nums[i]))
		ref[nums[i] + k] = nums[i]
	return len(set(count))

# 256. Paint House
# Input: [[17,2,17],[16,16,5],[14,3,19]]
# Output: 10
# Explanation: Paint house 0 into blue, paint house 1 into green, paint house 2 into blue. 
# Minimum cost: 2 + 5 + 3 = 10.

def mincost(costs):
	if not costs:
		return 0
	for i in range(1, len(costs)):
		costs[i][0] += min(costs[i-1][1],costs[i-1][2])
		costs[i][1] += min(costs[i-1][0],costs[i-1][2])
		costs[i][2] += min(costs[i-1][1],costs[i-1][2])
	return min(costs[-1])

#house = [[17,2,17],[16,16,5],[14,3,19]]
#print(mincost(house))

# University Career Fair
# arrival = [1,3,3,5,7], duration = [2,2,1,2,1]
# first company come at 1 stay for 2 hours
# two companies come at three, 1 stay for 2 hours 1 stay for 1 hour
# 1 company come at 5, stay for 2 hours
# 1 company come at 7 stay for 1 hour
# Output: 4

def careerFair(arrival, duration):

	timeLine = list(zip(arrival, duration))
	timeLine = sorted(timeLine, key=lambda x: (sum(x), x[1]))
	print(timeLine)
	res, end = 0, -float('inf')
	for arr, dur in timeLine:
		if arr >= end:
			res += 1
			end = arr + dur
	return res

arrival = [1,3,3,5,7]
duration = [2,2,1,2,1]
#print(careerFair(arrival, duration))

# Min discount problem
# In simple words, there is an array - prices array : [5, 4, 5, 1, 3, 3, 8, 2]

def minDiscount(prices):
	res = []
	for i, x in enumerate(prices):
		for j, y in enumerate(prices[i+1:], i+1):
			if y <= x:
				res.append(x - y)
				break
		else:
			res.append(x)
	return res

#print(minDiscount([5, 4, 5, 1, 3, 3, 8, 2]))

from bisect import bisect

def minDiscount_2(prices):
	n = len(prices)
	res = [0] * n
	c = []
	for i in range(n-1, -1, -1):
		while c and c[-1] > prices[i]:
			c.pop()
		res[i] = prices[i] - c[max(bisect(c, prices[i])-1,0)] if c else prices[i]
		c.append(prices[i])
	return res

#print(minDiscount_2([5, 4, 5, 1, 3, 3, 8, 2]))

def minDiscount_3(prices):
	mono_stack = []
	discount = {}

	for i, price in enumerate(prices):
		while mono_stack and prices[mono_stack[-1]] >= price:
			discount[mono_stack.pop()] = price
		mono_stack.append(i)

	res = [i for i in prices]
	for i in range(len(res)):
		if i in discount:
			res[i] -= discount.get(i)

	return res

#print(minDiscount_3([5, 4, 5, 1, 3, 3, 8, 2]))


#
#
# Activate Fountain
#

def activateFountain(A):
	if not A:
		return 0

	n = len(A)
	aux = list(range(n + 1))

	for i, x in enumerate(A, 1):
		aux[max(i - x, 1)] = min(i + x, n)

	ans, l, r = 0, 1, aux[1]
	while r <= n:
		new_r, ans = r, ans + 1
		while l <= r:
			new_r = max(new_r, aux[l])
			l += 1
		if l > n:
			break
		r = max(new_r, aux[l])
	return ans

#print(activateFountain([0,0,0,0,0]))

#
# Possible path
#

def possiblePath(a,b,x,y):

	def gcd(a, b):
		return a if b == 0 else gcd(b, a%b)

	return gcd(a, b) == gcd(x,y)

#print(possiblePath(3,3,1,1))

#
#
# Partition Array

def part(arr, k):
	length = len(arr)
	print (length//k)
	if length % k != 0:
		return False

	ref = {}
	for num in arr:
		if num in ref:
			ref[num] += 1
		else:
			ref[num] = 1

	print(ref.values())

	for item in ref.values():
		if item >= length // k:
			return False
	return True

#print(part([1,2,2,2], 3))


#
#
# Anagram Difference

def anaDiff(s1, s2):
	"""
	s1: list[str]
	s2: list[str]
	"""

	res = []
	for i in range(len(s1)):
		first = s1[i]
		second = s2[i]
		if len(first) != len(second):
			res.append(-1)
		else:
			count = 0
			char_count = [0] * 26

			for j in range(len(first)):
				char_count[ord(first[j]) - ord('a')] += 1

			for j in range(len(second)):
				char_count[ord(second[j]) - ord('a')] -= 1
				if char_count[ord(second[j]) - ord('a')] < 0:
					count += 1
			res.append(count)

	return res

print(anaDiff(['act', 'qsw'], ['cats','swq']))
