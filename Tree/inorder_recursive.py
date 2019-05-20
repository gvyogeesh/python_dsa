# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''
https://leetcode.com/problems/binary-tree-inorder-traversal/

Approach: Using recursion
'''     
class Solution(object):
    def __init__(self):
        self.result = []
    
    def inorderRecurUtil(self, root):
        if root == None:
            return
        self.inorderRecurUtil(root.left)
        self.result.append(root.val)
        self.inorderRecurUtil(root.right)
            
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.inorderRecurUtil(root)
        return self.result
