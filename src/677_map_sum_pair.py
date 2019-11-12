
class TrieNode(object):
	def __init__(self):
		self.children = {}
		self.value = None

class MapSum(object):
	def __init__(self):
		self.root = TrieNode()

	def insert(self, key, val):
		node = self.root
		for char in key:
			if char not in node.children:
				node.children[char] = TrieNode()
			node = node.children[char]
		node.value = val

	def sum(self, prefix):
		pass