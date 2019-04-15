'''
https://leetcode.com/problems/sliding-window-maximum/

Given an array nums, there is a sliding window of size k which 
is moving from the very left of the array to the very right. 
You can only see the k numbers in the window. 
Each time the sliding window moves right by one position. 
Return the max sliding window.

Example:

Input: nums = [1,3,-1,-3,5,3,6,7], and k = 3
Output: [3,3,5,5,6,7] 
Explanation: 
   

Window position                Max
--------------- 
               j               -----
[1  3  -1] -3  5  3  6  7       3
               j
 1 [3  -1  -3] 5  3  6  7       3
                  j
 1  3 [-1  -3  5] 3  6  7       5
                     j
 1  3  -1 [-3  5  3] 6  7       5
                          j
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7

 popleft = > Pop from front end
 pop => Pop from rear end
 append() => Insert from rear end

 appendleft() => Insert from front end

if not dq => queue is empty
'''
import collections

def findSlidingMax(arr, k):
	result = []
	# Iterate first k elements and process them
	dq = collections.deque()
	# [(1, 3) (2, -1)]
	for i in range(k):
		while dq and arr[i] > arr[dq[-1]]:
			dq.pop()

		dq.append(i)

	print(k, len(arr))
	for j in range(k,len(arr)):
		# Get the biggest ele for the previous window
		result.append(arr[dq[0]])
		# Check the validity of the window
		if j - dq[0] == k:
			dq.popleft()

		# Process j
		while(dq and arr[j] > arr[dq[-1]]):
			dq.pop()
		dq.append(j)
		print j

	result.append(arr[dq[0]])
	return result
		  # i
			# (7, 15)

def main():
		   # 0  1   2   3  4  5  6  7		  j
	arr =   [1, 3, -1, -3, 5, 13, 6, 15]
	k = 3
	result = findSlidingMax(arr, k)
	print(result)
if __name__ == "__main__":
	main()