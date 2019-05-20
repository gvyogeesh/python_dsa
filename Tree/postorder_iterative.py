# https://leetcode.com/problems/binary-tree-postorder-traversal/
# Approach: Iterative approach.

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
    
    def __init__(self):
        self.result = []
        
    def postorderRecurUtil(self, root):
        if root == None:
            return
        self.postorderRecurUtil(root.left)
        self.postorderRecurUtil(root.right)
        self.result.append(root.val)

        
        
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        prev = None
        cur = root
        mystk = Stack()
        while True:
            while cur != None:
                mystk.push(cur)
                cur = cur.left
                
            if mystk.isempty() == True:
                return self.result
            
            cur = mystk.top()
            if (cur.right == None or cur.right == prev):
                prev = cur
                self.result.append(cur.val)
                mystk.pop()
                cur = None
            else:
                prev = cur
                cur = cur.right
            
            
        return self.result
        
    
