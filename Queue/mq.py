class Queue:
	def __init__(self):
		self.items = []

	# Insert
	def enqueue(self, ele):
		self.items.append(ele)

#   Delete
	def dequeue(self):
		return self.items.pop(0)

	def isempty(self):

		if self.items == []:
			return True
		return False

	def size(self):
		return len(self.items)

	def __str__(self):
		return self.items

def main():
	mq = Queue()
	mq.enqueue(100)
	mq.enqueue(200)
	mq.enqueue(300)
	mq.enqueue(400)
	mq.enqueue(500)

	print mq.dequeue()
	print mq.dequeue()
	print mq.dequeue()
	print mq.dequeue()
	print mq.dequeue()


if __name__ == '__main__':
	main()