'''
https://leetcode.com/problems/binary-tree-pruning/
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pruneUtil(self, root):
        # 1st terminating cond
        if root == None:
            return None
        
#         leaf node + val == 0 , delete it
        
        
        root.left = self.pruneUtil(root.left)
        root.right = self.pruneUtil(root.right)
        
        if root.left == None and root.right == None and root.val == 0:
            return None
        
        return root
    
    def preorder(self, root):
        if root == None:
            return
        print(root.val)
        self.preorder(root.left)
        self.preorder(root.right)
        
    def pruneTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        print("Before")
        self.preorder(root)
        new_root =  self.pruneUtil(root)
        print("After")
        self.preorder(new_root)
        return new_root