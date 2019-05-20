# https://leetcode.com/problems/binary-tree-preorder-traversal/
# Definition for a binary tree node.

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.result = []
        

class Solution(object):
    def __init__(self):
        self.result = []
        
    def preorderUtil(self, root):
        if root == None:
            return 
     
        # print(root.val)
        self.result.append(root.val)
        self.preorderUtil(root.left)
        self.preorderUtil(root.right)
        
        
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.preorderUtil(root)
        return self.result
    