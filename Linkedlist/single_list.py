
class Node:
	def __init__(self, val):
		self.val = val
		self.next = None

class SingleList:
	def __init__(self):
		self.head = None
		self.size = 0

	def insert_rear(self, val):
		tmp = Node(val)
		self.size += 1
		if self.head == None:
			self.head = tmp
		else:
			cur = self.head
			while cur.next != None:
				cur = cur.next
			cur.next = tmp


	def insert_begin(self, val):
		tmp = Node(val)
		self.size += 1
		if self.head == None:
			self.head = tmp
		else:
			tmp.next = self.head
			self.head = tmp

	def delete_first(self):
		if self.head == None:
			print("List is empty!!")
			return
		self.size -= 1
		self.head = self.head.next


	def delete_last(self):
		if self.head == None:
			print("List is empty!!")
			return
		self.size -= 1
		
		cur = self.head
		prev = self.head

		while cur.next != None:
			prev = cur
			cur = cur.next

		# print("prev is {}".format(prev))
		# print("self.head is {} prev is {}".format(self.head, prev))
		if cur == self.head:
			self.head = None
			return
		prev.next = None
  

	def delete_pos(self, pos):
		if pos > self.size:
			print("Invalid position!!!")
			return

		if self.head == None:
			print("list is empty")
			return


		
		i = 1
		prev = cur = self.head

        # Handle only one element
		if cur == self.head and pos == 1 and self.size == 1:
			self.head = None
			return

		self.size -= 1
		while pos > i and cur.next != None:
			i += 1
			prev = cur
			cur = cur.next

		if prev == cur:
			self.head = cur.next
			print("printme")
		else:
			prev.next = cur.next


	def print_list(self):
		cur = self.head
		while cur != None:
			print(cur.val)
			cur = cur.next

	def find_val(self, value):
		cur = self.head
		while cur != None:
			if cur.val == value:
				print("success")
				return
			cur = cur.next

		print("failure")


def main():
	mylist = SingleList()
	# mylist.insert_begin(10)
	# mylist.insert_begin(20)
	# mylist.insert_begin(30)
	# mylist.insert_begin(40)
	# mylist.print_list()

	mylist.insert_rear(100)
	mylist.insert_rear(200)
	mylist.insert_rear(300)
	mylist.insert_rear(400)
	mylist.insert_rear(500)
	mylist.print_list()
	mylist.find_val(500)
	mylist.delete_pos(5)
	mylist.find_val(500)
	# print("After delte")
	# mylist.print_list()

	# print("After delete last")
	# mylist.delete_last()
	# mylist.print_list()
	# mylist.delete_last()
	# print("After delete")
	# mylist.print_list()
	# print("After delete front")
	# mylist.delete_first()
	# mylist.print_list()




if __name__ == "__main__":
	main()