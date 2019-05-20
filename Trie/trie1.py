class TrieNode:
    def __init__(self):
		self.isend = False
		self.children = [None] * 256
		self.word = None
        
class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
        for i in "Yogi":
            print i

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        cur = self.root
	    # for i in word:
        for i in word:
            # pass
			idx = ord(i)
			if cur.children[idx] == None:
				cur.children[idx] = TrieNode()

			cur = cur.children[idx]
        cur.word = word
        cur.isend = True
		
        

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        cur = self.root
        for i in word:
		# for i in word:
			idx = ord(i)
			if cur.children[idx] == None:
				# print("FAILURE: {} does not exists in trie".format(word))
				return False
			else:
				cur = cur.children[idx]
           
        if cur.isend == True and cur.word == word:
            return True
		


    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        cur = self.root
        for i in prefix:
			idx = ord(i)
			cur = cur.children[idx]
			if cur == None:
				return False
        return True



# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
