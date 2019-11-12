
class Solution(object):

	def calculateTime(self, keyboard, word):
		res, prev = 0, 0
		for char in word:
			idx = keyboard.index(char)
			res += abs(prev - idx)
			prev = idx
		return res

	def calculateTime_2(self, keyboard, word):
		res, prev = 0, 0
		ref = {}

		for idx, char in enumerate(keyboard):
			ref[char] = idx

		for char in word:
			res += abs(prev - ref[char])
			prev = ref[char]
		return res