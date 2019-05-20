'''
https://leetcode.com/problems/word-search-ii/

Given a dictionary, a method to do lookup in dictionary and a M x N 
board where every cell has one character. Find all possible words 
that can be formed by a sequence of adjacent characters.
Note that we can move to any of 8 adjacent characters, 
but a word should not have multiple instances of same cell.

Input: dictionary[] = {"GEEKS", "FOR", "QUIZ", "GO"};

       boggle[][]   = {{'G', 'I', 'Z'},
                       {'U', 'E', 'K'},
                       {'Q', 'S', 'E'}};

       output:  GEEKS QUIZ
         
'''
class Solution:
	def __init__(self):
		# print("hello")
		self.matrix = [['G', 'I', 'Z'],
					   ['U', 'E', 'K'],
					   ['Q', 'S', 'E']
					   ]
		# self.visited = [[0] * len(self.matrix)] * len(self.matrix)

		self.visited = [[0, 0, 0],
						[0, 0, 0],
						[0, 0, 0]
					   ]
		self.output = []
		self.words = ['GEEKS','GEEK', 'SKIU', 'QUIZ', 'FOR', "WORLD", "HELLO","ZESK", "IZKSQU"]

	def issafe(self, row, col):
		if row < 0 or row >= len(self.matrix):
			return False
		if col < 0 or col >= len(self.matrix[0]):
			return False

		if self.visited[row][col] == 1:
			return False

		return True

# Optimize this by using trie: todo 
	def isword(self, key):
		for i in self.words:
			if i == key:
				return True
		return False

	def dfsutil(self, i, j, key):
		self.visited[i][j] = 1
		key.append(self.matrix[i][j])

		keystr = "".join(key)
		if self.isword(keystr) == True:
			self.output.append(keystr)

		# Explore all of its 8 neighbors.
		#                N       NE       E      SE      S        SW         W      NW       
		directions = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
		for direction in directions:
			row = direction[0]
			col = direction[1]
			if self.issafe(row + i , col + j): 
				self.dfsutil(row + i, col + j, key)
		# End instructions before return
		self.visited[i][j] = 0
		if key:
			# print(key)
			key.pop()



	def word_search(self):
		for i in range(len(self.matrix)):
			for j in range(len(self.matrix[0])):
				if self.visited[i][j] == 0:
					self.dfsutil(i , j, [])
		print("Words can be formed from boggle are {}".format(self.output))

def main():
	obj = Solution()
	obj.word_search()

if (__name__ == "__main__"):
	main()
