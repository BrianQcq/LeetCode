from collections import OrderedDict

class LRUCache(object):

	def __init__(self, capacity):
		self.cache = OrderedDict()
		self.size = capacity

	def get(self, key):
		if key not in self.cache:
			return -1
		val = self.cache.pop(key)
		self.cache[key] = val
		return val

	def put(self, key, value):
		if key in self.cache:
			self.cache.pop(key)
		self.cache[key] = value
		if len(self.cache) > self.size:
			self.cache.popitem(last=False)


"""
Using deque and dict
"""
from collections import deque
class LRU(object):

	def __init__(self, capacity):
		self.q = deque([])
		self.ref = {}
		self.size = capacity

	def get(self, key):
		if key not in self.ref:
			return -1
		self.q.remove(key)
		self.q.append(key)
		return self.ref[key]

	def put(self, key, value):
		if key in self.ref:
			self.ref.pop(key)
			self.q.remove(key)
		elif len(self.ref) == self.size:
			k = self.q.popleft()
			self.ref.pop(k)
		self.ref[key] = value
		self.q.append(key)

"""
Using Dict and Double-Linked List
"""
class Node(object):
	def __init__(self, key, value):
		self.key = key
		self.value = value
		self.prev = None
		self.next = None

class LRU_Double_LinkedList(object):
	def __init__(self, capacity):
		self.cache = {}
		self.size = capacity
		self.head = Node(0,0)
		self.tail = Node(0,0)
		self.head.next = self.tail
		self.tail.prev = self.head

	def get(self, key):
		if key not in self.cache:
			return -1
		n = self.cache[key]
		self._remove(n)
		self._add(n)
		return n.value

	def put(self, key, value):
		if key in self.cache:
			self._remove(self.cache[key])
		n = Node(key, value)
		self._add(n)
		self.cache[key] = n
		if len(self.cache) > self.size:
			node = self.head.next
			self._remove(node)
			self.cache.pop(node.key)

	def _remove(self, node):
		p = node.prev
		n = node.next
		p.next = n
		n.prev = p

	def _add(self, node):
		p = self.tail.prev
		p.next = node
		self.tail.prev = node
		node.prev = p
		node.next = self.tail
