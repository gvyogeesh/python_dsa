'''
https://leetcode.com/problems/copy-list-with-random-pointer/
'''

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if head == None:
            return
        
        cur = head
        
        while cur != None:
            # print "first"
            nextptr = cur.next
            cur.next = Node(cur.val, None, None)
            cur1 = cur.next
            cur1.next = nextptr
            cur = nextptr
        
        cur = head
        head1 = cur1 = head.next
        
        # while cur != None:
        #     print cur.val, cur.random.val
        #     if cur.next:
        #         cur = cur.next.next
            
        
        while cur != None:
            # print "Second"
            if cur.random:
                print cur.random.val
                print cur.random.next.val
            if cur.random:
                cur1.random = cur.random.next
            cur = cur1.next
            if cur:
                cur1 = cur.next
        
        
        cur = head
        cur1 = cur.next
        
#         while cur1 != None:
#             print cur1.val, cur1.random.val
            
#             cur1 = cur1.next.next
        
        while cur != None:
            # print "Third"
            cur.next = cur1.next
            if cur.next:
                cur1.next = cur.next.next
            
            cur = cur.next
            if cur:
                cur1 = cur.next
        
        return head1
        