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

class Solution1:
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
Runtime 30 ms Beats 91.36% of users with Python3
Memory 16.82 MB Beats 51.62% of users with Python3
"""
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        arr = []
        while head != None:
            arr.append(head.val)
            head = head.next

        while left < right:
            arr[left - 1], arr[right - 1] = arr[right - 1], arr[left - 1]
            left += 1
            right -= 1

        def arrayToList(arr, n):
            root = None
            for i in range(0, n, 1):
                root = insert(root, arr[i])

            return root

        def insert(root, value):
            temp = ListNode(value)

            if (root == None):
                root = temp
            else:
                ptr = root
                while (ptr.next != None):
                    ptr = ptr.next
                ptr.next = temp
            return root

        n = len(arr)
        root = arrayToList(arr, n)

        return root

"""
Submissions:
Runtime 38 ms Beats 50.75% of users with Python3
Memory 16.66 MB Beats 75.51% of users with Python3
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