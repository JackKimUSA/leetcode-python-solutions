#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 03:10:27 2020

@author: Jack Kim
"""

"""
Problem:
Reverse a singly linked list.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution_1:
    def reverseList(self, head: ListNode) -> ListNode:
        def reverse(node: ListNode, prev: ListNode = None):
            if not node:
                return prev
            next, node.next = node.next, prev
            return reverse(next, node)
        return reverse(head)

"""
Submissions:
Runtime: 40 ms, faster than 24.02% of Python3 online submissions for Reverse Linked List.
Memory Usage: 20.4 MB, less than 5.06% of Python3 online submissions for Reverse Linked List.
"""

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        node, prev = head, None
        
        while node:
            next, node.next = node.next, prev
            prev, node = node, next
        return prev
"""
Submissions:
Runtime: 36 ms, faster than 61.40% of Python3 online submissions for Reverse Linked List.
Memory Usage: 15.7 MB, less than 30.81% of Python3 online submissions for Reverse Linked List.
"""