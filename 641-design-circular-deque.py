#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 21:10:27 2020

@author: Jack Kim
"""

"""
Problems:
Design your implementation of the circular double-ended queue (deque).

Your implementation should support following operations:

  - MyCircularDeque(k): Constructor, set the size of the deque to be k.
  - insertFront(): Adds an item at the front of Deque. Return true if the operation is successful.
  - insertLast(): Adds an item at the rear of Deque. Return true if the operation is successful.
  - deleteFront(): Deletes an item from the front of Deque. Return true if the operation is successful.
  - deleteLast(): Deletes an item from the rear of Deque. Return true if the operation is successful.
  - getFront(): Gets the front item from the Deque. If the deque is empty, return -1.
  - getRear(): Gets the last item from Deque. If the deque is empty, return -1.
  - isEmpty(): Checks whether Deque is empty or not. 
  - isFull(): Checks whether Deque is full or not.
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.left=None
        self.right=None



class MyCircularDeque:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self.head, self.tail = ListNode(None), ListNode(None)
        self.k,self.len = k, 0
        self.head.right,self.tail.left = self.tail, self.head

    def _add(self, node:ListNode, new:ListNode):
        n = node.right
        node.right = new
        new.left, new.right = node, n
        n.left=new

    def _del(self, node:ListNode):
        n = node.right.right
        node.right = n
        n.left = node

    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        if self.len == self.k:
            return False
        self.len += 1
        self._add(self.head, ListNode(value))
        return True

    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        if self.len == self.k:
            return False
        self.len += 1
        self._add(self.tail.left, ListNode(value))
        return True


    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        if self.len == 0:
            return False
        self.len -= 1
        self._del(self.head)
        return True

    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        if self.len == 0:
            return False
        self.len -=1
        self._del(self.tail.left.left)
        return True

    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """
        return self.head.right.val if self.len else -1

    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """
        return self.tail.left.val if self.len else -1

    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        return self.len == 0

    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        return self.len == self.k

"""
Submissions:
Runtime: 76 ms, faster than 32.20% of Python3 online submissions for Design Circular Deque.
Memory Usage: 15.1 MB, less than 16.10% of Python3 online submissions for Design Circular Deque.

"""
mycd=MyCircularDeque(3)
print(mycd.isEmpty())
print(mycd.insertFront(1))
print(mycd.isEmpty())
print(mycd.insertFront(2))
print(mycd.getFront())
print(mycd.insertLast(3))
print(mycd.getRear())
print(mycd.insertLast(4))
print(mycd.getRear())
print(mycd.deleteLast())
print(mycd.insertLast(4))
print(mycd.getRear())
print(mycd.deleteFront())
print(mycd.insertLast(4))
print(mycd.getRear())
print(mycd.isFull())
print(mycd.deleteFront())
print(mycd.getFront())
print(mycd.isFull())




