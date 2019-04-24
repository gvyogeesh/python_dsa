'''
https://leetcode.com/problems/intersection-of-two-linked-lists/
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getlength(self, head):
        length = 0
        cur = head
        while cur != None:
            length += 1
            cur = cur.next
        return length
        
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        length1 = self.getlength(headA)
        length2 = self.getlength(headB)
        print("L1 = {} L2 = {}".format(length1, length2))
        
        while length1 > length2:
            headA = headA.next
            length1 -= 1
            
        while length2 > length1:
            headB = headB.next
            length2 -= 1
        
        while headA != None and headB != None:
            if headA == headB:
                return headA
            else:
                headA = headA.next
                headB = headB.next
        