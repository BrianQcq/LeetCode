
class Solution(object):

	def shortestDis(self, words, word1, word2):
		ref = {}
		for i, word in enumerate(words):
			if word in ref:
				ref[word].append(i)
			else:
				ref[word] = [i]

		curMin = float('inf')
		for i in ref[word1]:
			for j in ref[word2]:
				if abs(i-j) < curMin:
					curMin = abs(i-j)
		return curMin

	def shortestDis_2(self, words, word1, word2):
		res = idx1 = idx2 = len(words)

		for i in range(len(words)):
			if words[i] == word1:
				idx1 = i
				res = min(res, abs(idx1 - idx2))
			elif words[i] == word2:
				idx2 = i
				res = min(res, abs(idx1 - idx2))
		return res