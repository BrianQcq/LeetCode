
class Solution(object):

	def isAlienSorted(self, words, order):
		ref = {char: idx for idx, char in enumerate(order)}
		words = [[ref[c] for c in word] for word in words]

		return all(w1 <= w2 for w1, w2 in zip(words, words[1:]))

	def isAlienSorted_w(self, words, order):

		ref = {char: idx for idx, char in enumerate(order)}

		for i in range(len(words)-1):
			word1 = words[i]
			word2 = words[i+1]

			for j in range(min(len(word1, len(word2)))):
				if word1[j] != word2[j]:
					if ref[word1[j]] > ref[word2[j]]:
						return False
					break
			else:
				if len(word1) > len(word2):
					return False
		return True