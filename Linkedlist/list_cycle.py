'''
https://leetcode.com/problems/linked-list-cycle/
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None:
            return False
        
        slowptr = fastptr = head
        while (slowptr.next and fastptr.next and fastptr.next.next):
            slowptr = slowptr.next
            fastptr = fastptr.next.next
            
            if slowptr == fastptr:
                return True
        return False