class TrieNode:
	def __init__(self):
		self.children = [None] * 256
		self.isend = False
		self.word = None
		# for i in range(256):
		# 	self.chidren.append(None)

class Trie:
	def __init__(self):
		self.root = TrieNode()

	def insert(self, word):
		cur = self.root
		for i in word:
			# print("Idx:{} Letter: {}".format(ord(i), i))
			idx = ord(i)
			if cur.children[idx] == None:
				cur.children[idx] = TrieNode()
			cur = cur.children[idx]
		cur.isend = True
		cur.word = word
				
		

	def search(self, word):
		''' True if exists else False'''
		cur = self.root
		for i in word:
			idx = ord(i)
			if cur.children[idx] == None:
				return False
			cur = cur.children[idx]

		if cur.isend == True:
			return True
		else:
			return False

	def print_trie_util(self, root):
		if root == None:
			return

		if root.isend == True:
			print(root.word)

		for i in range(256):
			if root.children[i] == None:
				continue

			if root.children[i] != None:
				self.print_trie_util(root.children[i])


	def autocomplete(self, prefix):
		cur = self.root
		for i in prefix:
			idx = ord(i)
			if cur.children[idx] == None:
				print("No words exists with prefix {}".format(prefix))
				return
			cur = cur.children[idx]

		self.print_trie_util(cur)

	def is_delete(self, root):
		for i in range(256):
			if root.children[i] != None:
				return False
		return True

	def delete_util(self, root, sidx, eidx, key):
		if sidx == eidx:
			root.isend = False
			if  self.is_delete(root):
				return True
			else:
				return False
		else:
			idx = ord(key[sidx])
			# print("Sidx {} endidx {}".format(idx, eidx))
			if self.delete_util(root.children[idx], sidx+1, eidx, key):
				print("Sidx {} endidx {}".format(sidx, eidx))
				# True condition
				root.children[idx] = None
				if root.isend == True or self.is_delete(root) == False:
					return False
	
				return True
			else:
				return False


	def delete_word(self, word):
		self.delete_util(self.root, 0, len(word), word)

	def print_trie(self):
		self.print_trie_util(self.root)

def main():
	tr = Trie()
	tr.insert("r")

	tr.insert("risk")
	tr.delete_word("r")
	tr.delete_word("risk")
	tr.insert("google")
	tr.insert("goa")
	tr.insert("goal")
	tr.insert("goat")
	tr.insert("golang")
	tr.insert("goooo")
	tr.print_trie()
	print("After deletion")
	# tr.delete_word("goat")
	tr.delete_word("goa")
	tr.print_trie()
	# tr.insert("ga")
	# tr.insert("all")
	# tr.insert("bat")
	# tr.insert("cat")
	# tr.insert("dog")
	# tr.insert("how mongo db works ******)*%%GHJJJJfds473243927")
	# tr.insert("how redis db works")
	# tr.insert("how cassandra  works")
	# tr.insert("how to calculate pf")
	# tr.insert("how to find average")
	# tr.print_trie()
	# print(tr.search("google"))
	# print(tr.search("goo"))
	# print(tr.search("goa"))
	# print(tr.search("hello world"))
	# tr.autocomplete("how")
	# tr.autocomplete("g")
	# tr.insert("abcdefABCDE12334+_)}?&%*")
	# tr.insert("golang")
	# tr.insert("goa")
	# tr.insert("goal")
	# tr.print_trie()
	# tr.search('google')
	# tr.delete_word("google")
	# tr.search('google')


if __name__ == "__main__":
	main()