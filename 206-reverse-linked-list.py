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

class Solution_2:
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

class Solution_3:
    def reverseList(self, head: ListNode) -> ListNode:
        prev=None
        while head:
            temp=head
            head=head.next
            temp.next=prev
            prev=temp
        return prev
"""
Submissions:
Runtime: 40 ms, faster than 26.82% of Python3 online submissions for Reverse Linked List.
Memory Usage: 15.6 MB, less than 45.01% of Python3 online submissions for Reverse Linked List.
"""

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev=None
        while head:
            temp, head = head, head.next
            temp.next, prev = prev, temp
        return prev

"""
Submissions:
Runtime: 36 ms, faster than 62.49% of Python3 online submissions for Reverse Linked List.
Memory Usage: 15.6 MB, less than 45.01% of Python3 online submissions for Reverse Linked List.
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
prev=S.reverseList(head)

while prev:
    print(prev.val)
    prev = prev.next