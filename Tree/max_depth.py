'''
https://leetcode.com/problems/maximum-depth-of-binary-tree/
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

   
class Solution(object):
    def maxDepthUtil(self, root):
        if root == None:
            return 0
        left = self.maxDepthUtil(root.left)
        right = self.maxDepthUtil(root.right)
        return 1 + max(left, right)
            
    
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.maxDepthUtil(root)
        