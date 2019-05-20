# https://leetcode.com/problems/binary-tree-postorder-traversal/
# Approach: Recursion

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


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
        self.postorderRecurUtil(root)
        return self.result