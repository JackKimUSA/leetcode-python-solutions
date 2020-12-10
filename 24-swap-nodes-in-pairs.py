#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 09 21:10:27 2020

@author: Jack Kim
"""

"""
Problems:
Given a linked list, swap every two adjacent nodes and return its head.

You may not modify the values in the list's nodes. Only nodes itself may be changed.
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution_1:
    def swapPairs(self, head: ListNode) -> ListNode:
        cur = head

        while cur and cur.next:
            cur.val, cur.next.val = cur.next.val, cur.val
            cur = cur.next.next

        return head

"""
Submissions:
Runtime: 32 ms, faster than 55.52% of Python3 online submissions for Swap Nodes in Pairs.
Memory Usage: 14.2 MB, less than 46.11% of Python3 online submissions for Swap Nodes in Pairs
"""


class Solution_2:
    def swapPairs(self, head: ListNode) -> ListNode:
        root = prev = ListNode(None)
        prev.next = head
        while head and head.next:
            b = head.next
            head.next = b.next
            b.next = head

            prev.next = b

            head = head.next
            prev = prev.next.next
        return root.next

"""
Submissions:
Runtime: 32 ms, faster than 55.52% of Python3 online submissions for Swap Nodes in Pairs.
Memory Usage: 14.2 MB, less than 18.84% of Python3 online submissions for Swap Nodes in Pairs.
"""


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head and head.next:
            p = head.next

            head.next = self.swapPairs(p.next)
            p.next = head
            print(p.val)
            return p
        return head

"""
Submissions:
Runtime: 32 ms, faster than 55.52% of Python3 online submissions for Swap Nodes in Pairs.
Memory Usage: 14.3 MB, less than 18.84% of Python3 online submissions for Swap Nodes in Pairs.
"""

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)

node1.next = node2
node2.next = node3
node3.next = node4


head=node1

S = Solution()
head=(S.swapPairs(head))

while head:
    print(head.val)
    head = head.next