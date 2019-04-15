'''
Build Min Heap
'''

class MinHeap:
	def __init__(self, capacity):
		self.size = 0
		self.capacity = capacity
		self.arr = [None] * capacity
		

	def left_child(self, i):
		return (2 * i) + 1

	def right_child(self, i):
		return (2 * i) + 2

	def parent(self, i):
		return (i - 1)/2

	def getmin(self):
		return self.arr[0]

	def insert(self, item):
		self.size += 1
		self.arr[self.size - 1] = item

		i = self.size -1
	
		while i > 0:
		   par = self.parent(i)
		   if self.arr[par] > self.arr[i]:
				# swap parent & child
				tmp = self.arr[i]
				self.arr[i] = self.arr[par]
				self.arr[par] = tmp

				i = self.parent(i)
		   else:
				break

	def heapify(self, idx):
		i = idx
		small = i
		lc = self.left_child(i)
		rc = self.right_child(i)

		if lc < self.size and self.arr[small] > self.arr[lc]:
			small = lc

		if rc < self.size and self.arr[small] > self.arr[rc]:
			small = rc

# Swap i and small
		if small != i :
			tmp = self.arr[i]
			self.arr[i] = self.arr[small]
			self.arr[small] = tmp

			self.heapify(small)




	def extractmin(self):
		item = self.arr[0]
		last_idx = self.size -1
		cur_idx = 0

# Swap last and current(0th) idx
		tmp = self.arr[last_idx]
		self.arr[last_idx] = self.arr[cur_idx]
		self.arr[cur_idx] = tmp

		self.size -= 1
		self.heapify(cur_idx)

		return item

	def delidx(self, idx):
		ele = self.arr[idx]
		self.arr[idx] = -float("inf")
		i = idx

		while i > 0:
			par = self.parent(i)
			if self.arr[par] > self.arr[i]:
				# swap parent & child
				tmp = self.arr[i]
				self.arr[i] = self.arr[par]
				self.arr[par] = tmp

				i = self.parent(i)

		self.extractmin()

		return ele

def main():
	min_heap = MinHeap(7)
	min_heap.insert(20)
	min_heap.insert(40)
	min_heap.insert(50)
	min_heap.insert(5)
	min_heap.insert(60)
	min_heap.insert(3)
	min_heap.insert(1)

	print (min_heap.arr)
	print(min_heap.delidx(3))

	print(min_heap.arr[0:min_heap.size])
	# print(min_heap.extractmin())
	# print(min_heap.arr[0:min_heap.size])
	# print(min_heap.extractmin())
	# print(min_heap.arr[0:min_heap.size])
	# min_heap.insert(4)
	# print(min_heap.arr[0:min_heap.size])

     

if __name__ == "__main__":
	main()