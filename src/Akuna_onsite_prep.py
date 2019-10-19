# 295. Find Median from Data Stream

# addNum(1)
# addNum(2)
# findMedian() -> 1.5
# addNum(3) 
# findMedian() -> 2

# Follow up:

# If all integer numbers from the stream are between 0 and 100, how would you optimize it?
# If 99% of all integer numbers from the stream are between 0 and 100, how would you optimize it?
from bisect import *
class MedianFinder_naive(object):

	def __init__(self):
		self.arr = []
		self.size = 0

	def addNum(self, num):
		idx = bisect_left(self.arr, num)
		self.arr.insert(idx, num)
		self.size += 1

	def findMedian(self):
		if self.size % 2 == 0:
			return (self.arr[self.size//2] + self.arr[self.size//2 - 1]) / 2.0
		else:
			return self.arr[self.size//2]


from heapq import *
class MedianFinder(object):

	def __init__(self):
		self.small = []
		self.large = []

	def addNum(self, num):
		if len(self.small) == 0:
			heappush(self.small, -num)
			return
		if num <= -self.small[0]:
			heappush(self.small, -num)
		else:
			heappush(self.large, num)

		if len(self.small) - len(self.large) == 2:
			heappush(self.large, -heappop(self.small))
		elif len(self.small) - len(self.large) == -2:
			heappush(self.small, -heappop(self.large))

	def findMedian(self):
		if len(self.small) == len(self.large):
			return (self.large[0] - self.small[0]) / 2.0
		return -float(self.small[0]) if len(self.small) > len(self.large) else float(self.large[0])



# 713. Subarray Product Less Than K
# Input: nums = [10, 5, 2, 6], k = 100
# Output: 8
# Explanation: The 8 subarrays that have product less than 100 are: [10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6].
# Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.

class Solution_713(object):

	def numSubarrProductLessThanK(self, nums, k):
		if k <= 1:
			return 0
		prod = 1
		res = l = 0
		for r, val in enumerate(nums):
			prod *= val
			while prod >= k:
				prod /= nums[l]
				l += 1
			res += r - l + 1
		return res



# 1177. Can Make Palindrome from Substring
# Input: s = "abcda", queries = [[3,3,0],[1,2,0],[0,3,1],[0,3,2],[0,4,1]]
# Output: [true,false,false,true,true]

# Prefix Sum
class Solution_1177(object):

	def canMakePaliQueries(self, s, queries):
		cnt = [[0] * 26]
		print(cnt)
		print('==========')

		for i, c in enumerate(s):
			cnt.append(cnt[i][:])
			cnt[i+1][ord(c)-ord('a')] += 1
			print(cnt)

		return [sum((cnt[hi + 1][i] - cnt[lo][i]) % 2 for i in range(26)) // 2 <= k for lo, hi, k in queries]

test = Solution_1177()
res = test.canMakePaliQueries('abcda', [[3,3,0],[1,2,0],[0,3,1],[0,3,2],[0,4,1]])
print(res)



# 1048. Longest String Chain
# Input: ["a","b","ba","bca","bda","bdca"]
# Output: 4
# Explanation: one of the longest word chain is "a","ba","bda","bdca".

class Solution_1048(object):

	def longestStrChain(self, words):
		words = sorted(words, key=len)
		word_dict = {}
		for word in words:
			word_dict[word] = 1

		res = 1
		for word in words:
			for i in range(len(word)):
				if word[:i] + word[i+1:] in word_dict:
					word_dict[word] = word_dict[word[:i] + word[i+1:]] + 1
					res = max(res, word_dict[word])
		return res