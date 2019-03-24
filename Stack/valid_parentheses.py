'''
https://leetcode.com/problems/valid-parentheses/
'''
class Stack:
	def __init__(self):
		self.items = []
		# self.top = -1
	
	def push(self,ele):
		self.items.append(ele)

	def pop(self):
		if self.isempty() == False:
			return self.items.pop()

	def size(self):
		return len(self.items)

	def isempty(self):
		if self.items == []:
			return True
		else:
			return False

	def top(self):
		return self.items[-1]

def isValidParenthesis(inp_str):
	mystk = Stack()
	for i in inp_str:
		if i in ["{","(", "["]:
			mystk.push(i)
		else:
			if i == "}":
				if mystk.isempty():
					return False
				top_ele = mystk.top()
				if top_ele != "{":
					return False
				mystk.pop()

			elif i == ")":
				if mystk.isempty():
					return False
				top_ele = mystk.top()
				if top_ele != "(":
					return False
				mystk.pop()

			elif i == "]":
				if mystk.isempty():
					return False
				top_ele = mystk.top()
				if top_ele != "[":
					return False
				mystk.pop()

	if mystk.isempty() == False:
		return False

	return True

print isValidParenthesis("()[{}]")

'''
Following code has been uploaed to leetcode to test all test cases:
class Stack:
	def __init__(self):
		self.items = []
		# self.top = -1
	
	def push(self,ele):
		self.items.append(ele)

	def pop(self):
		if self.isempty() == False:
			return self.items.pop()

	def size(self):
		return len(self.items)

	def isempty(self):
		if self.items == []:
			return True
		else:
			return False

	def top(self):
		return self.items[-1]
    
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def isValidParenthesis(inp_str):
            mystk = Stack()
            for i in inp_str:
                if i in ["{","(", "["]:
                    mystk.push(i)
                else:
                    if i == "}":
                        if mystk.isempty():
                            return False
                        top_ele = mystk.top()
                        if top_ele != "{":
                            return False
                        mystk.pop()

                    elif i == ")":
                        if mystk.isempty():
                            return False
                        top_ele = mystk.top()
                        if top_ele != "(":
                            return False
                        mystk.pop()

                    elif i == "]":
                        if mystk.isempty():
                            return False
                        top_ele = mystk.top()
                        if top_ele != "[":
                            return False
                        mystk.pop()

            if mystk.isempty() == False:
                return False

            return True
        return isValidParenthesis(s)
'''
