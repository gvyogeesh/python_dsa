# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

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
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        mystk = Stack()
        cur = root
        
        while True:
            while cur != None:
                mystk.push(cur)
                cur = cur.left
            
            if mystk.isempty() == True:
                return result
            
            cur = mystk.top()
            result.append(cur.val)
            mystk.pop()
            cur = cur.right
        
        