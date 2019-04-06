'''
Minimum time required to rot all oranges
Given a matrix of dimension m*n where each cell in the matrix can 
have values 0, 1 or 2 which has the following meaning:
0: Empty cell
1: Cells have fresh oranges
2: Cells have rotten oranges
 So we have to determine what is the minimum time required so that all the 
 oranges become rotten. A rotten orange at index [i,j] can rot other 
 fresh orange at indexes up, down, left and right. If it is impossible
  to rot every orange then simply return -1.
Examples:
Input:  arr[][C] = { {2, 1, 0, 2, 1},
                     {1, 0, 1, 2, 1},
                     {1, 0, 0, 2, 1}};
Output:
All oranges can become rotten in 2 time frames.
'''
import mq
def isvalid(arr, row, col):
	if row < 0 or row >= len(arr):
		return False
	if col < 0 or col >= len(arr[0]):
		return False

	# print ("Isvalid row = {} col {}".format(row, col))
	if arr[row][col] == 1:
		return True

	return False

def check_cells(arr):
	for i in range(len(arr)):
		for j in range(len(arr[i])):
			if arr[i][j] ==1:
				return False
	return True

def isrotten(arr):
	myq = mq.Queue()
	days = 0
	# Iterate complete 2d array to get rotten oranges
	for i in range(len(arr)):
		for j in range(len(arr[i])):
			if arr[i][j] ==2:
				myq.enqueue((i, j))
	# print myq.items

	while(myq.isempty() == False):
		size = myq.size()
		found = False
		while size > 0:
			row, col = myq.dequeue()
			# North
			if(isvalid(arr, row-1, col)):
				
				found = True
				arr[row-1][col] = 2
				myq.enqueue((row-1, col))

			# South
			if(isvalid(arr, row+1, col)):
				found = True
				arr[row+1][col] = 2
				myq.enqueue((row+1, col))

			# West
			if(isvalid(arr, row, col-1)):
				found = True
				arr[row][col-1] = 2
				myq.enqueue((row, col-1))


			# East
			if(isvalid(arr, row, col+1)):
				found = True
				arr[row][col+1] = 2
				myq.enqueue((row, col+1))

			size = size -1

		if found:
			days += 1

	if check_cells(arr):
		return days
	return -1

def main():
	# 3 days
	arr = [[1, 2, 1],
		   [0, 2, 2],
		   [2, 1, 0]]

		 
	print (isrotten(arr))

if __name__ == "__main__":
	main()