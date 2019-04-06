'''
Implement Circular queue
'''

class CircularQueue():
	def __init__(self, size):
		self.max_size = size
		self.items = [None for i in range(size)]
		self.front = -1
		self.rear = -1
		
	def enqueue(self, ele):
		if self.isfull():
			print("Queue is Full...")
			return

		if self.front == -1 and self.rear == -1:
			self.front = self.rear = 0
			self.items[self.rear] = ele

		else:
			self.rear = (self.rear + 1) % self.max_size
			self.items[self.rear] = ele

	def dequeue(self):
		if self.isempty() == True:
			print("Queue is Empty...")
			return
		data = self.items[self.front]
		if self.front == self.rear:
			self.front = -1
			self.rear = -1
		else:
			self.front = (self.front + 1) % self.max_size

		return data

	def isempty(self):
		if self.front == -1 and self.rear == -1:
			return True
		return False

	def isfull(self):
		if (self.rear + 1) % self.max_size == self.front:
			return True

		return False 

def main():
	mcq = CircularQueue(5)
	mcq.enqueue(100)
	mcq.enqueue(200)
	mcq.enqueue(300)
	mcq.enqueue(400)
	mcq.enqueue(500)
	print mcq.dequeue()
	mcq.enqueue(5000)
	print mcq.dequeue()
	print mcq.dequeue()

	print mcq.dequeue()
	print mcq.dequeue()
	print mcq.dequeue()
	print mcq.dequeue()

if __name__ == "__main__":
	main()