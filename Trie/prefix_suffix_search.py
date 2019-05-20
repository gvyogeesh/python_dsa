'''
https://leetcode.com/problems/prefix-and-suffix-search/
'''
class TrieNode:
	def __init__(self):
		self.isend = False
		self.children = {}
		self.word = None
        
class Trie:
    def __init__(self):
		self.root = TrieNode()
        
    def print_trie(self, prefix):
        cur = self.root
        for i in prefix:
            if i not in cur.children:
                return []
            cur = cur.children[i]
        words = []
        self.printutil(cur, words)
        # print "Words are {}".format(words)
        return words
        
    def printutil(self, root, words):
        if root.isend == True:
            words.append(root.word)
        for key, val in root.children.items():
            self.printutil(val, words)
    
    def insert(self, word):
		cur = self.root
		for i in word:
			if i not in cur.children:
				cur.children[i] = TrieNode()
			cur = cur.children[i]
		cur.isend = True
		cur.word = word
		
            
class WordFilter(object):

    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.word_dict = {}
        self.prefix_trie = Trie()
        self.suffix_trie = Trie()
        self.prefix_cache = {}
        self.suffix_cache = {}
        
        # for i  in range(len(words)):
            # 
        for i  in range(len(words)):
            self.word_dict[words[i]] = i
            self.prefix_trie.insert(words[i])
            self.suffix_trie.insert(words[i][::-1])
        
        # print self.word_dict
        self.prefix_trie.print_trie("ap")
        self.suffix_trie.print_trie("hs")

    def f(self, prefix, suffix):
        """
        :type prefix: str
        :type suffix: str
        :rtype: int
        """
        prefixwords = self.prefix_trie.print_trie(prefix)
        print suffix
        suffixwords = [word[::-1] for word in self.suffix_trie.print_trie(suffix[::-1])]
        # print("Yogeesha")
        # print suffixwords
        
        match_words = set(prefixwords) & set(suffixwords)
        # print match_words
        
        # print ("Pfx words are {}".format(prefixwords))
        # print("Sfx words are {}".format(suffixwords))
        
        result = -1
        for i in match_words:
            if self.word_dict[i] > result:
                result = self.word_dict[i]
        return result
        


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)
