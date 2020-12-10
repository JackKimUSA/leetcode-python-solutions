#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 09 21:10:27 2020

@author: Jack Kim
"""

"""
Problem:
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each of their nodes contains a single digit. 
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution_1:
    def reverseList(self, head: ListNode) -> ListNode:
        node, prev = head, None

        while node:
            next, node.next = node.next, prev
            prev, node = node, next

        return prev

    def toList(self, node: ListNode) -> ListNode:
        list: List = []
        while node:
            list.append(node.val)
            node = node.next
        return list

    def toReversedLinkedList(self, result: ListNode) -> ListNode:
        prev: ListNode = None
        for r in result:
            node = ListNode(r)
            node.next = prev
            prev = node

        return node

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        a = self.toList(self.reverseList(l1))
        b = self.toList(self.reverseList(l2))

        #resultStr = int(''.join(str(e) for e in a)) + int(''.join(str(e) for e in b))
        resultStr = int(''.join(map(str,a))) + int(''.join(map(str,b)))
        return self.toReversedLinkedList(str(resultStr))
"""
Submissions:
Runtime: 84 ms, faster than 8.11% of Python3 online submissions for Add Two Numbers.
Memory Usage: 14.5 MB, less than 14.62% of Python3 online submissions for Add Two Numbers.
"""


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        root = head = ListNode(0)

        carry = 0

        while l1 or l2 or carry:
            sum = 0

            if l1:
                sum += l1.val
                l1 = l1.next
            if l2:
                sum += l2.val
                l2 = l2.next

            carry, val = divmod(sum + carry, 10)
            head.next = ListNode(val)
            head = head.next

        return root.next

"""
Submissions:
Runtime: 72 ms, faster than 50.04% of Python3 online submissions for Add Two Numbers.
Memory Usage: 14.1 MB, less than 88.51% of Python3 online submissions for Add Two Numbers.
"""

node1 = ListNode(2)
node2 = ListNode(4)
node3 = ListNode(3)

node1.next = node2
node2.next = node3

nodea = ListNode(5)
nodeb = ListNode(6)
nodec = ListNode(4)

nodea.next = nodeb
nodeb.next = nodec

S = Solution_1()
head=S.addTwoNumbers(node1, nodea)
while head:
    print(head.val)
    head = head.next
