'''
There are a number of plants in a garden. Each of these plants has been treated
 with some amount of pesticide. After each day, if any plant has more pesticide 
 than the plant on its left, being weaker than the left one, it dies.

You are given the initial values of the pesticide in each of the plants. 
Print the number of days after which no plant dies, i.e. the time after which 
there are no plants with more pesticide content than the plant to their left.

For example, pesticide levels . Using a -indexed array, day  plants  and  die 
leaving . On day , plant  of the current array dies leaving . As there is no 
plant with a higher concentration of pesticide than the one to its left, plants 
stop dying after day .

Input: 6 5 8 4 7 10 9
Answer: 2
'''