'''
A Maze is given as N*N binary matrix of blocks where source block
 is the upper left most block i.e., maze[0][0] and destination block
  is lower rightmost block i.e., maze[N-1][N-1]. 
  A rat starts from source and has to reach the destination. 
  The rat can move only in two directions: forward and down.
In the maze matrix, 0 means the block is a dead end and 1 means 
the block can be used in the path from source to destination. 
Note that this is a simple version of the typical Maze problem.
 For example, a more complex version can be that the rat can move in 
 4 directions and a more complex version can be with a limited number
  of moves.
                {1, 0, 0, 0}
                {1, 1, 0, 1}
                {0, 1, 0, 0}
                {1, 1, 1, 1}

 '''
class Solution:
 	

	def __init__(self):

 		self.maze = [[1, 1, 1, 1],
 					 [1, 1, 1, 1],
 					 [1, 1, 1, 1],
 					 [1, 1, 1, 1]
 					]
 		self.counter = 0
 		self.result = [[0] * len(self.maze) for i in range(len(self.maze))]
 		# print self.result

 	def issafe(self, row, col):
 		if row < 0 or row > len(self.maze) - 1:
 			return False

 		if col < 0 or col >len(self.maze[0]) - 1:
 			return False

 		if self.maze[row][col] == 0:
 			return False

 		return True


 	def findpath(self, row, col):
 		self.result[row][col] = 1
 		if row == len(self.maze) - 1 and col == len(self.maze[0]) - 1:
 			self.counter = self.counter + 1
 			print("Solution {} is {}".format(self.counter, self.result))
 			# print self.result

 		else:
 			
 			# Explore to right side
 			if self.issafe(row, col + 1) == True:
 				self.findpath(row, col + 1)

 			# Exploret to bottom side
 			if self.issafe(row + 1, col) == True:
 				self.findpath(row + 1, col)

 		self.result[row][col] = 0

def main():
	obj = Solution()
	obj.findpath(0, 0)
	print("Total number of solutions are {}".format(obj.counter))
if __name__ == "__main__":
 	main()