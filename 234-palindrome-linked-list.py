#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 01:34:42 2020

@author: Jack Kim
"""

"""
Problem:
Given a singly linked list, determine if it is a palindrome.
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution_1:
    def isPalindrome(self, head: ListNode) -> bool:
        q=[] # List
            
        if not head:
            return True
        
        node = head
        
        while node is not None:
            q.append(node.val)
            node=node.next
        
        while len(q) > 1:
            if q.pop(0) != q.pop():
                return False
        return True

"""
Submissions:
Runtime: 156 ms, faster than 5.58% of Python3 online submissions for Palindrome Linked List.
Memory Usage: 24.4 MB, less than 13.01% of Python3 online submissions for Palindrome Linked List.
"""
# Deque
import collections

class Solution_2:
    def isPalindrome(self, head: ListNode) -> bool:
        q= collections.deque() # Deque
            
        if not head:
            return True
        
        node = head
        
        while node is not None:
            q.append(node.val)
            node=node.next
        
        while len(q) > 1:
            if q.popleft() != q.pop():
                return False
        return True

"""
Submissions:
Runtime: 72 ms, faster than 50.92% of Python3 online submissions for Palindrome Linked List.
Memory Usage: 24.3 MB, less than 15.01% of Python3 online submissions for Palindrome Linked List.
""" 

# Runner
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        rev = None
        slow = fast = head
        
        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next
        if fast:
            slow = slow.next
        
        while rev and rev.val == slow.val:
            slow, rev = slow.next, rev.next
        return not rev

"""
Submissions:
Runtime: 68 ms, faster than 74.22% of Python3 online submissions for Palindrome Linked List.
Memory Usage: 24.2 MB, less than 36.21% of Python3 online submissions for Palindrome Linked List.
"""

node1=ListNode(1)
node2=ListNode(2)
node3=ListNode(2)
node4=ListNode(1)

node1.next=node2
node2.next=node3
node3.next=node4

head=node1
#while head:
#    print(head.val)
#    head = head.next
    
S=Solution()
print(S.isPalindrome(head))
