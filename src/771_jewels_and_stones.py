
class Solution(object):

	def numJewelsInStones(self, J, S):
		jewel = []
		count = 0

		for char in J:
			jewel.append(char)
		for stone in S:
			if stone in jewel:
				count += 1

		return count