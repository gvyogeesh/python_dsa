'''
Find the number of islands:
Given a boolean 2D matrix, find the number of islands. 
A group of connected 1s forms an island. For example,
 the below matrix contains 5 islands
Input : mat[][] = {{1, 1, 0, 0, 0},
                   {0, 1, 0, 0, 1},
                   {1, 0, 0, 1, 1},
                   {0, 0, 0, 0, 0},
                   {1, 0, 1, 0, 1}
Output : 5
'''

class Solution:
	def __init__(self):
		# print("hello")
		self.matrix = [[1, 1, 0, 0, 0],
					   [0, 1, 0, 0, 1],
					   [1, 0, 1, 1, 1],
					   [1, 0, 1, 0, 1],
					   [1, 0, 1, 0, 1]
					   ]
		# self.visited = [[0] * len(self.matrix)] * len(self.matrix)

		self.visited = [[0, 0, 0, 0, 0],
					    [0, 0, 0, 0, 0],
					   [0, 0, 0, 0, 0],
					   [0, 0, 0, 0, 0],
					   [0, 0, 0, 0, 0]
					   ]
		self.counter = 0

	def count_islands(self):
		for i in range (len(self.matrix)):
			for j in range(len(self.matrix[0])):
				# print("CI method i={}, j={} visited {} matrix {} ".format(i, j, self.visited[i][j], self.matrix[i][j]))
				# if (((self.matrix[i][j] == 1 and self.visited[i][j] == 0)):
				if self.matrix[i][j] == 1:
					if self.visited[i][j] == 0:
						# print("Calling from main")
						self.dfsutil(i, j)
						self.counter = self.counter + 1
		return self.counter

	def issafe(self, row, col):
		if row < 0 or row >= len(self.matrix):
			return False
		if col < 0 or col >= len(self.matrix[0]):
			return False

		if self.visited[row][col] == 1 or self.matrix[row][col] == 0:
			return False

		return True

	def dfsutil(self, r, c):
		# print("dfsutil")
		self.visited[r][c] = 1

		#                N       NE       E      SE      S        SW         W      NW       
		directions = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
		for i in directions:
			row = i[0]
			col = i[1]
			if self.issafe(row +r , col +c):
			# if self.matrix[row + r][col + c] == 1 and self.visited[row + r][col + c] == 0:
				self.dfsutil(row + r, col + c)
 

def main():
	obj = Solution()
	print("Number of islands are {}".format(obj.count_islands()))

if __name__ == "__main__":
	main()
