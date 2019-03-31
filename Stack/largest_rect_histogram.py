'''
Given n non-negative integers representing the histogram's
 bar height where the width of each bar is 1, find the area of
 largest rectangle in the histogram.
https://leetcode.com/problems/largest-rectangle-in-histogram/

Input: [2,1,5,6,2,3]
Output: 10
'''
# O(N * N)
import mystk
def largest_rectangle(arr):
	result = 0
	for i in range(len(arr)):
		left = 0
		right = 0
		for j in (i-1, -1, -1):
			if arr[j] >= arr[i]:
				left += 1
			else:
				break
		for k in (i+1, len(arr)):
			# print (i , k)
			if k < len(arr) and arr[k] >= arr[i]:
				right += 1
			else:
				break

		cur_result = arr[i]* (left + right + 1) 
		if result < cur_result:
			result = cur_result
	print result

def largest_rectangle_skt(arr):
	i = 0
	stk = mystk.Stack()
	# print len(arr)
	result = 0
	while i < len(arr):
		while stk.isempty() == False and arr[i] < arr[stk.top()]:
			cur = stk.pop()
			if stk.isempty() == False:
				distance = i - stk.top() - 1
			else:
				distance = i
			cur_area = arr[cur] * distance
			if cur_area > result:
				result = cur_area

		stk.push(i)
		i = i + 1
	while (stk.isempty() == False):
		cur = stk.pop()
		if stk.isempty() == False:
				distance = i - stk.top() - 1
		else:
			distance = i
		cur_area = arr[cur] * distance
		if cur_area > result:
			result = cur_area

	print result

if __name__ == "__main__":
	arr = [2,1,5,6,2,3]
	# arr = [5, 7, 8, 4]
	largest_rectangle(arr)
	largest_rectangle_skt(arr)

		
