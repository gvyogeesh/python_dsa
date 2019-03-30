
'''


Various signal towers are present in a city.
Towers are aligned in a straight horizontal line(from left to right) and
 each tower transmits a signal in the right to left direction.
 Tower A shall block the signal of Tower B if Tower A is present to the left of 
 Tower B and Tower A is taller than Tower B. So,the range of a signal of a given 
 tower can be defined as :

{(the number of contiguous towers just to the left of the given tower whose height
 is less than or equal to the height of the given tower) + 1}.

You need to find the range of each tower.
Example: 
Input: 100 80 60 70 60 75 85
Output: 1 1 1 2 1 4 6
'''
# O(N * N) => O(N)
import mystk
def signal_range_bruteforce(arr):
	result = [1] * len(arr)

	# for i in range(len(arr)):
	# 	result.append(0)
	# result [0] = 1

	for i in range(1,len(arr)):
		for j in range(i-1,-1,-1):
			if arr[j] <= arr[i]:
				result[i] = result[i] + 1
			else:
				break

		# print "Marker"
	print result

def signgal_range_stk(arr):
	stk = mystk.Stack()
	result = [0] * len(arr)
	i = 0
	while i < len(arr):
		# Check whether stack has elements and if  cur ele is bigger than
		# top ele, keep popping
		while(stk.isempty() == False and arr[i] >= arr[stk.top()]):
			stk.pop()

		if stk.isempty():
			result[i] = i + 1
		else:
			result[i] = i - stk.top()

		stk.push(i)
		i = i + 1

	print result


def main(): 
	                    # i
	                    # j
     #      0    1   2   3   4
	# arr = [100, 80, 60, 85, 120]

	arr = [100, 80, 60, 70, 60, 75, 85]   
			# 1    1   1   2   1   4   6     
	print("Bruteforce method:")
	signal_range_bruteforce(arr)
	print("Stack based solution :")
	signgal_range_stk(arr)
if __name__ == '__main__':
	main()