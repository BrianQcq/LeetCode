import re
import collections


class Solution(object):

	def mostCommonWord(self, para, banned):
		ban = set(banned)
		words = re.findall(r'\w+', para.lower())
		return collections.Counter(w for w in words if w not in ban).most_common(1)[0][0]