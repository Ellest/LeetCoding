class RecipientTracker:

	def __init__(self, recipients, k):
		self.counts = {}
		self.initial_load(recipients)
		self.heap_map = {}
		self.heap = [None] * k
		self.K = k

	"""
	# MISC
	"""

	def get_info(self):
		print("This Tracker is keeping track of top", self.cnts, "recipients")
		print("Current number of distinct recipients:", len(self.counts))

	"""
	# Recipients processing

	"""
	def initial_load(self, recipients):
		for r in recipients:
			self.counts[r] = self.counts.get(r, 0) + 1
		## TODO
		#	- Logic for initializing heap. K max elements

	def email(self, r):
		self.counts[r] = self.counts.get(r, 0) + 1
		if r in self.heap_map:
			self.heapify(self.heap_map[r])
		elif self.counts[r] > self.get_min():
			del self.heap_map[self.heap[0]] # delete from map to indicate it's no longer in the heap
			self.heap[0] = r
			self.heap_map[r] = 0
			self.heapify()

	"""
	# Heap Operations 

	"""
	def heap_swap(self, i, j):
		self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
		self.heap_map[self.heap[i]], self.heap_map[self.heap[j]] = i, j
	
	def get_parent(self, i):
		return (i - 1) // 2
	
	def left_child(self, i):
		return 2 * i + 1

	def right_child(self, i):
		return 2 * i + 2

	def heapify(self, i = 0):
		if not self.heap or i >= self.K: return False
		l, r, s = self.left_child(i), self.right_child(i), i
		if l < len(self.heap) and self.counts[self.heap[l]] < self.counts[self.heap[s]]:
			s = l
		if r < len(self.heap) and self.counts[self.heap[r]] < self.counts[self.heap[s]]:
			s = r
		if s != i
			self.heap_swap(s, i)
			self.heapify(s) # recursively heapify
		return True

	def heapify_up(self, i):
		if not self.heap or i >= self.K: return False
		p = self.get_parent(i)
		while i > 0 and self.counts[self.heap[i]] < self.counts[self.heap[p]]:
			self.heap_swap(i, p)
			i, p = p, self.get_parent(p)

	def increase_key(self, r, v = None):
		if r not in self.heap_map: return False
		val = v or 1
		heapify(self.heap_map[r])
		return True

	def get_min(self):
		if not self.heap: 
			print("Heap Underflow")
			return None 
		return self.heap[0]

	def extract_min(self):
		temp = self.heap[0]

