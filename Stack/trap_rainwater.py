'''
Given n non-negative integers representing an elevation map where 
the width
 of each bar is 1, compute how much water it is able to trap after 
 raining.
For example,
Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6

https://leetcode.com/problems/trapping-rain-water/
'''
import mystk
def trap_water(arr):
	result = 0
	for i in range(len(arr)):
		rb = 0
		lb = 0
		# Traverse left hand side & get the tallest element 
		for j in range(i,-1,-1):
			if arr[j] > lb:
				lb = arr[j]

		for k in range(i, len(arr), 1):
			if arr[k] > rb:
				rb = arr[k]
		# print("Left bigger ele = {} Rigt bigger ele is {}".format(lb, rb))
		result = result + min(lb, rb) - arr[i]
		# Traverse right hand side & get the tallest element
	print result

def trap_water_stk(arr):
	result = 0
	i = 0
	stk = mystk.Stack()
	while i < len(arr):
		while(stk.isempty() == False and arr[i] > arr[stk.top()]):
			cur = stk.pop()
			if stk.isempty() == True:
				break

			height = min(arr[i], arr[stk.top()]) - arr[cur]
			width = i - stk.top() - 1 
			# print("heigh * width {} for i {}".format(height * width, i))
			# print(" i = {} heigh {} width {}".format(i, height, width))
			result = result + (height * width)
		stk.push(i)
		# print("i while pushing {}".format(i))
		i = i + 1
	print result

def main():
	     # 0  8  7  8  0  2  3  0
	          # 1     1  
	# 
	arr = [0,1,0,2,1,0,1,3,2,1,2,1]
	arr = [100, 0, 89, 46, 0, 0, 89]
	trap_water(arr)
	trap_water_stk(arr)
if __name__ == "__main__":
	main()