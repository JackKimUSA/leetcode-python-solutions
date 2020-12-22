#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 21:10:27 2020

@author: Jack Kim
"""

"""
Problems:
Design your implementation of the circular queue. 
The circular queue is a linear data structure in which the operations are performed based 
on FIFO (First In First Out) principle and the last position is connected back to the first position 
to make a circle. It is also called "Ring Buffer".

One of the benefits of the circular queue is that we can make use of the spaces in front of the queue. 
In a normal queue, once the queue becomes full, we cannot insert the next element even if there is a space 
in front of the queue. But using the circular queue, we can use the space to store new values.

Implementation the MyCircularQueue class:

  - MyCircularQueue(k) Initializes the object with the size of the queue to be k.
  - int Front() Gets the front item from the queue. If the queue is empty, return -1.
  - int Rear() Gets the last item from the queue. If the queue is empty, return -1.
  - boolean enQueue(int value) Inserts an element into the circular queue. Return true 
    if the operation is successful.
  - boolean deQueue() Deletes an element from the circular queue. Return true if the operation is successful.
  - boolean isEmpty() Checks whether the circular queue is empty or not.
  - boolean isFull() Checks whether the circular queue is full or not.
"""

class MyCircularQueue:

    def __init__(self, k: int):
        self.q=[None] * k
        self.maxlen = k
        self.p1 = 0
        self.p2 = 0

    def enQueue(self, value: int) -> bool:
        if self.q[self.p2] is None:
            self.q[self.p2] = value
            self.p2 = (self.p2 + 1) % self.maxlen
            return True
        else:
            return False

    def deQueue(self) -> bool:
        if self.q[self.p1] is None:
            return False
        else:
            self.q[self.p1] = None
            self.p1 = (self.p1 + 1) % self.maxlen
            return True


    def Front(self) -> int:
        return -1 if self.q[self.p1] is None else self.q[self.p1]

    def Rear(self) -> int:
        return -1 if self.q[self.p2 - 1 ] is None else self.q[self.p2 - 1]

    def isEmpty(self) -> bool:
        return self.p1 == self.p2 and self.q[self.p1] is None

    def isFull(self) -> bool:
        return self.p1 == self.p2 and self.q[self.p1] is not None
"""
Submissions:
Runtime: 60 ms, faster than 97.32% of Python3 online submissions for Design Circular Queue.
Memory Usage: 14.6 MB, less than 54.23% of Python3 online submissions for Design Circular Queue.
"""
mycq=MyCircularQueue(3)
print(mycq.enQueue(1))
print(mycq.enQueue(2))
print(mycq.enQueue(3))
print(mycq.enQueue(3))
print(mycq.Rear())
print(mycq.isFull())
print(mycq.deQueue())
print(mycq.enQueue(4))
print(mycq.Rear())




