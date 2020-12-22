#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 21:10:27 2020

@author: Jack Kim
"""

"""
Problems:
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.
"""

import heapq
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists) -> ListNode:
        root = result = ListNode(None)
        heap = []
        
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i, lists[i]))
        while heap:
            node = heapq.heappop(heap)
            idx = node[1]
            result.next = node[2]

            result = result.next
            if result.next:
                heapq.heappush(heap, (result.next.val, idx, result.next))
        return root.next


"""
Submissions:
Runtime: 100 ms, faster than 74.47% of Python3 online submissions for Merge k Sorted Lists.
Memory Usage: 18.1 MB, less than 44.49% of Python3 online submissions for Merge k Sorted Lists.
"""

node1 = ListNode(1)
node2 = ListNode(4)
node3 = ListNode(5)

node1.next = node2
node2.next = node3

nodea = ListNode(1)
nodeb = ListNode(3)
nodec = ListNode(4)

nodea.next = nodeb
nodeb.next = nodec

nodex = ListNode(2)
nodey = ListNode(6)

nodex.next = nodey

lists=[node1, nodea, nodex]

S=Solution()
head=S.mergeKLists(lists)

while head:
    print(head.val)
    head = head.next

