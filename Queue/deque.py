class DeQueue:
	def __init__(self):
		self.items = []

	# Insert
	def enqueue_rear(self, ele):
		self.items.append(ele)

#   Delete
	def dequeue_front(self):
		return self.items.pop(0)

	def enqueue_front(self, ele):
		self.items.insert(0, ele)

	def dequeue_rear(self):
		return self.items.pop()


	def isempty(self):

		if self.items == []:
			return True
		return False

	def size(self):
		return len(self.items)

def main():
	mq = DeQueue()
	mq.enqueue_rear(100)
	mq.enqueue_rear(200)
	mq.enqueue_rear(300)
	mq.enqueue_rear(400)

	print mq.dequeue_front()
	print mq.dequeue_front()
	print mq.dequeue_front()
	print mq.dequeue_front()

	print("Version 2")
	mq.enqueue_front(100)
	mq.enqueue_front(200)
	mq.enqueue_front(300)
	mq.enqueue_front(400)

	print mq.dequeue_rear()
	print mq.dequeue_rear()
	print mq.dequeue_rear()
	print mq.dequeue_rear()
	
if __name__ == '__main__':
	main()