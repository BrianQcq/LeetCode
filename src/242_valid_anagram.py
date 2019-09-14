
class Solution(object):

	def validAnagram(self, s, t):

		ref = {}
		for i in s:
			if i not in ref:
				ref[i] = 1
			else:
				ref[i] += 1
		for j in t:
			if i not in ref:
				return False
			else:
				ref[i] -= 1
		for value in ref.values():
			if value != 0:
				return False
		else return True