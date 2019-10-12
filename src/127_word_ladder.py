from collections import deque
import string
class Solution(object):

	def ladderLength(self, beginWord, endWord, wordList):
		arr = set(wordList)
		q = deque([(beginWord, 1)])
		visited = set()
		alpha = string.ascii_lowercase

		while q:
			word, length = q.popleft()
			if word == endWord:
				return length

			for i in range(len(word)):
				for char in alpha:
					newWord = word[:i] + char + word[i+1:]
					if newWord in arr and newWord not in visited:
						q.append((newWord, length+1))
						visited.add(newWord)
		return 0