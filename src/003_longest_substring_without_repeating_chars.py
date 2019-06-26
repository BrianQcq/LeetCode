"""
Given a string, find the length of the longest substring without repeating characters

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""

class Solution(object):
	def lengthOfLongestSubstring(self, s):
		used = {}
		max_length = start = 0
		for i, ch in enumerate(s):
			if ch in used and start <= used[ch]:
				start = used[ch] + 1
			else:
				max_length = max(max_length, i - start + 1)

			used[ch] = i

		return max_length

A=Solution()
res=A.lengthOfLongestSubstring("bbbbcbcbb")
print(res)

"""
Unfinished!!!
"""