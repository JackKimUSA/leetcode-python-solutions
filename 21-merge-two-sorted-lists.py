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

class Solution:
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
