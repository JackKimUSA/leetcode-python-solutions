#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 02:02:21 2020

@author: Jack Kim
"""

"""
Problem:
Merge two sorted linked lists and return it as a new sorted list. 
The new list should be made by splicing together the nodes of the first two lists.
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution_1:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if (not l1) or (l2 and l1.val > l2.val):
            l1, l2 = l2, l1
        if l1:
            l1.next = self.mergeTwoLists(l1.next, l2)
        return l1

"""
Submissions:
Runtime: 40 ms, faster than 37.26% of Python3 online submissions for Merge Two Sorted Lists.
Memory Usage: 14.1 MB, less than 40.53% of Python3 online submissions for Merge Two Sorted Lists.
"""

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(0)
        ptr = head

        while True:
            if l1 is None and l2 is None:
                break
            elif l1 is None:
                ptr.next = l2
                break
            elif l2 is None:
                ptr.next = l1
                break
            else:
                smallerVal = 0
                if l1.val < l2.val:
                    smallerVal = l1.val
                    l1 = l1.next
                else:
                    smallerVal = l2.val
                    l2 = l2.next

                newNode = ListNode(smallerVal)
                ptr.next = newNode
                ptr=ptr.next
        return head.next
"""
Submissions:
Runtime: 36 ms, faster than 72.07% of Python3 online submissions for Merge Two Sorted Lists.
Memory Usage: 14.3 MB, less than 8.83% of Python3 online submissions for Merge Two Sorted Lists.
"""

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(4)

nodea = ListNode(1)
nodeb = ListNode(3)
nodec = ListNode(4)

node1.next = node2
node2.next = node3

nodea.next = nodeb
nodeb.next = nodec

S = Solution()
head=S.mergeTwoLists(node1, nodea)

while head:
    print(head.val)
    head = head.next
