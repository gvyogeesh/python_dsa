'''
Recursively remove all adjacent duplicates:
Input: careermonk
Output: camonk

Input: mississippi
Output: m
'''
def removeAdjDup(inp_str):
	# print "Begin"
	top = -1
	i = 0
	inp_list = list(inp_str)
	size = len(inp_list)
	while i < size:
		if top == -1 or inp_list[top] != inp_list[i]:
			# print inp_list
			top += 1
			inp_list[top] = inp_list[i]
			i = i + 1
		else:
			while i < size and inp_list[top] == inp_list[i]:
				i += 1
			top = top -1

	# print top

	return "".join(inp_list[0:top+1])

def main():

	print (removeAdjDup("mississippin"))

if __name__ == "__main__":
	main()