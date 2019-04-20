# https://leetcode.com/problems/merge-k-sorted-lists/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

import heapq
# heapq.heappush()
# heapq.heappop() -> Extract Min
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        myheap = []
        head = prev = None
        for i in range(len(lists)):
            # print (lists[i].val, lists[i])
            if lists[i]:
                heapq.heappush(myheap, (lists[i].val, lists[i]))
        
        if myheap:
            head = myheap[0][1]
            prev = head
            print("Prev and Head are {}".format(prev))
            heapq.heappop(myheap)
            if head.next != None:
                heapq.heappush(myheap, (head.next.val, head.next))
        
        while myheap:
            cur = myheap[0][1]
            heapq.heappop(myheap)
            prev.next = cur
            prev = cur
            if cur.next != None:
                heapq.heappush(myheap, (cur.next.val, cur.next))
        return head
            