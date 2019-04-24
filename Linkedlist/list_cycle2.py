'''
https://leetcode.com/problems/linked-list-cycle-ii/
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return 
        
        slowptr = fastptr = head
        while (slowptr.next and fastptr.next and fastptr.next.next):
            slowptr = slowptr.next
            fastptr = fastptr.next.next
            
            if slowptr == fastptr:
                p1 = head
                p2 = slowptr
                
                while p1 != p2:
                    p1 = p1.next
                    p2 = p2.next
                return p1
                
        return 