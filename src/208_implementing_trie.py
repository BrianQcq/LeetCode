
class Trie:

	def __init__(self):
		self.trie = {}

	def insert(self, word):
		t = self.trie
		for char in word:
			if char not in t:
				t[char] = {}
			t = t[char]
		t['#'] = '#'

	def search(self, word):
		t = self.trie
		for char in word:
			if char not in t:
				return False
			t = t[char]
		return '#' in t

	def startwith(self, prefix):
		t = self.trie
		for char in prefix:
			if char not in t:
				return False
			t = t[char]
		return True

test=Trie()
test.insert('apple')
print(test.trie)