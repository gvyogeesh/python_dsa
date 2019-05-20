'''
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        
        path1 = []
        path2 = []
        def findPath(root, key, path):
            if root == None:
                return False
            
            path.append(root)
            if root == key:
                return True
            
            left = findPath(root.left, key, path)
            right = findPath(root.right, key, path)
            
            if left == True or right == True:
                return True
            path.pop()
            return False
            
            
        
        l1 = findPath(root, p, path1)
        l2 = findPath(root, q, path2)
        
        if l1 == False or l2 == False:
            return None
        i = 0
        while True:
            try:
                if path1[i] != path2[i]:
                    return path1[i-1]
                
            except IndexError:
                return path1[i-1]
            i += 1
        
            
            
        for i in path1:
            if i != None:
                print i.val
                
        print("Q is: ")
        for i in path2:
             if i != None:
                print i.val
                
        # print path1
        
        