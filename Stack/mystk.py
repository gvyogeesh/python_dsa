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


def main():
	mystk = Stack()
	# 100, 200, 300 
	mystk.push(100)
	mystk.push(200)
	mystk.push(300)
	mystk.push(400)
	mystk.push(500)

	print mystk.top()
	print mystk.size()
	print mystk.pop()
	print mystk.top()
	print mystk.size()
	print mystk.pop()
	print mystk.top()
	print mystk.pop()
	print mystk.pop()
	print mystk.pop()
	print mystk.pop()
	
if __name__ == "__main__":
	 main()