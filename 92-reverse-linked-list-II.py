#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 10 21:10:27 2020

@author: Jack Kim
"""

"""
Problems:
Reverse a linked list from position m to n. Do it in one-pass.

Note: 1 ≤ m ≤ n ≤ length of list.
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if not head or m == n:
            return head

        root = start = ListNode(None)
        root.next = head

        for _ in range(m - 1):
            start = start.next
        end = start.next

        for _ in range(n - m):
            tmp, start.next, end.next = start.next, end.next, end.next.next
            start.next.next = tmp
        return root.next

"""
Submissions:
Runtime: 32 ms, faster than 56.76% of Python3 online submissions for Reverse Linked List II.
Memory Usage: 14.6 MB, less than 6.89% of Python3 online submissions for Reverse Linked List II.
"""
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5


head=node1

S = Solution()
m , n = 2, 4
head=(S.reverseBetween(head, m, n))

while head:
    print(head.val)
    head = head.next