


'''
Albus Dumbledore announced that the school will host the legendary
event known as Wizard Tournament where four magical schools are
going to compete against each other in a very deadly competition by
facing some dangerous challenges. Since the team selection is very
critical in this deadly competition. Albus Dumbledore asked Little Monk
to help him in the team selection process. There is a long queue
of students from all the four magical schools. Each student of a school
have a different roll number. Whenever a new student will come,
he will search for his schoolmate from the end of the queue.
As soon as he will find any of the schoolmate in the queue,
he will stand behind him, otherwise he will stand at the end of the queue.
At any moment Little Monk will ask the student, who is standing in front of
 the queue,
to come and put his name in the Goblet of Fire and remove him from the queue.

                      sid   rn
Sample input : [('E', 1,    1), ('E', 2, 0), ('E', 1, 2), ('D'), ('D')]

Output: (1, 1), (1, 2)

'''
import mq
def solve_challenge(arr):
	main_queue = mq.Queue()
	result = []

	school_queue = [mq.Queue() for i in range(5)]
	print(len(school_queue))
	for i in arr:
		if i[0] == 'E':
			print("Enqueue operation!!!")
			sid = i[1] 
			roll_num = i[2]
			if school_queue[sid].isempty() == True:
				main_queue.enqueue(sid)
			school_queue[sid].enqueue(roll_num)
			

		elif i[0] == 'D':
			print ("Dequeue")
			sid = main_queue.front()
			roll_num = school_queue[sid].dequeue()

			result.append((sid, roll_num))
			if school_queue[sid].isempty() == True:
				main_queue.dequeue()

	print "Sub queues"
	# print school_queue
	print result
def main():
	# inp_arr = [('E', 1, 1), ('E', 1, 2), ('E', 2, 10), ('E', 3, 10),('E', 1, 15), ('E', 2, 100), ('D'), ('D'), ('D'), ('D'), ('D'), ('D')]
	inp_arr = [('E', 1, 100), ('E', 2, 100), ('E', 3, 90), ('E', 1, 90),('E', 2, 200),('D'),('D'),('D'),('D'),('D')]
	solve_challenge(inp_arr)

if __name__ == "__main__":
        main()