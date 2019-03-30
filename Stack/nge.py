'''Next Greater Element:


Given an array, print the Next Greater Element (NGE) for every element. 
The Next greater Element for an element x is the first greater element on
 the right side of x in array. Elements for which no greater element exist, 
 consider next greater element as -1.

Examples:
a) For any array, rightmost element always has next greater element as -1.
b) For an array which is sorted in decreasing order, all elements 
have next greater element as -1.
c) For the input array [4, 5, 2, 25}, the next greater elements for each 
element are as follows.
Element       NGE
   4      -->   5
   5      -->   25
   2      -->   25
   25     -->   -1
d) For the input array [13, 7, 6, 12}, the next greater elements
 for each element are as follows.

  Element        NGE
   13      -->    -1
   7       -->     12
   6       -->     12
   12     -->     -1
 '''
# O(N^2)
Bruteforce method:
100 => -1
80 => 85
60 => 70
70 => 75
60 => 75
75 => 85
85 => -1
Stack based solution :
100 => -1
80 => 85
60 => 70
70 => 75
60 => 75
75 => 85
85 => -1
import mystk
def nge_bruteforce(arr):
	result = [-1] * len(arr)
	# print result
	for i in range(len(arr)):
		for j in range(i+1, len(arr)):
			if arr[j] > arr[i]:
				# print("{} = > {}".format(arr[i], arr[j]))
				result[i] = arr[j]
				break

		# print ("Marker")
	for i in range(len(arr)):
		print("{} => {}".format(arr[i], result[i]))
	# print result

def nge_stk(arr):
	stk = mystk.Stack()
	i = 0
	result = [-1] * len(arr)
	while i < len(arr):
		# If stack is not empty and current ele is > top ele, keep popping and 
		# Compute the answer for popped element
		while stk.isempty() == False and arr[i] > arr[stk.top()]:
			cur = stk.pop()
			result[cur] = arr[i]

		stk.push(i)
		i = i + 1
	for i in range(len(arr)):
		print("{} => {}".format(arr[i], result[i]))
	# while stk.isempty() == False:
	# 	cur = stk.pop()
	# 	result[cur] = -1
def main(): 
	                    # i
	                    # j
     #      0    1   2   3   4
	# arr = [100, 80, 60, 85, 120]

	arr = [100, 80, 60, 70, 60, 75, 85]   
			# 1    1   1   2   1   4   6     
	print("Bruteforce method:")
	nge_bruteforce(arr)
	print("Stack based solution :")
	nge_stk(arr)
if __name__ == '__main__':
	main()