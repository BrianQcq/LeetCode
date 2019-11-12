from threading import Lock

class Foo(object):

	def __init__(self):
		self.firstDone = Lock()
		self.secondDone = Lock()
		self.firstDone.acquire()
		self.secondDone.acquire()

	def first(self, printFirst):
		printFirst()
		self.firstDone.release()

	def second(self, printSecond):
		with self.firstDone:
			printSecond()
			self.secondDone.release()

	def third(self, printThird):
		with self.secondDone:
			printThird()