import heapq
def main():

	listForTree = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
	heapq.heapify(listForTree)             # for a min heap
	heapq._heapify_max(listForTree)

if __name__ == "__main__":
	main()