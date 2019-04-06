'''
Implement queue using stack
'''

class Stack:
	def __init__(self):
		self.items = []
		# self.top = -1
	
	def push(self,ele):
		self.items.append(ele)

	def pop(self):
		if self.isempty() == False:
			return self.items.pop()

	def size(self):
		return len(self.items)

	def isempty(self):
		if self.items == []:
			return True
		else:
			return False

	def top(self):
		return self.items[-1]


class Queue_Stk:
	def __init__(self):
		self.st1 = Stack()
		self.st2 = Stack()

	def enqueue(self, ele):
		self.st1.push(ele)

	def dequeue(self):
		if self.st2.isempty():
			# Transfer all elements from st1 to st2
			while(self.st1.isempty() == False):
				self.st2.push(self.st1.pop())
		return self.st2.pop()


	def isempty(self):
		if (self.st1.isempty() == True and self.st2.isempty() == True):
			return True
		return False

	def size(self):
		return (self.st1.size()) + self.st2.size()
mq = Queue_Stk()
if mq.isempty():
	print("Empty")
mq.enqueue(100)
mq.enqueue(200)
mq.enqueue(300)
mq.enqueue(400)

print mq.size()
print mq.dequeue()
print mq.dequeue()
print mq.dequeue()
print mq.dequeue()

print mq.dequeue()


