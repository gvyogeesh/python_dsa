'''



Suppose there is a circle. There are  petrol pumps on that circle.
Petrol pumps are numbered 0 to N-1 (both inclusive).

You have two pieces of information corresponding to each of the petrol 
pump: (1) the amount of petrol that particular petrol pump will give,
and (2) the distance from that petrol pump to the next petrol pump.

Initially, you have a tank of infinite capacity carrying no petrol.
You can start the tour at any of the petrol pumps. Calculate the first
point from where the truck will be able to complete the circle.
Consider that the truck will stop at each of the petrol pumps. 
The truck will move one kilometer for each litre of the petrol.

1 5
10 3
3 4

This problem need not requrie queue but understanding queue concept helps in 
breaking down the solution.
'''

def truck_tour(arr):
	size = len(arr)

	for i in range(len(arr)):
		# print arr[i][0], arr[i][1]
		count = 0
		rem_distance = 0
		for j in range(i, i + len(arr)+1):
			# print(i, j%size)
			rem_distance += arr[j%size][0] - arr[j%size][1]
			if rem_distance < 0:
				break
			count += 1
			# print(count)

			if count == len(arr):
				return i

			

	return 

if __name__ == "__main__":
			        # i
			 # 0       1        2
	arr = [(1, 5), (2, 3), (30, 4)]
	                 # j
	print(truck_tour(arr))