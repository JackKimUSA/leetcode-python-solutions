#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 21:10:27 2020

@author: Jack Kim
"""

"""
Problems:
Implement a last in first out (LIFO) stack using only two queues. 
The implemented stack should support all the functions of a normal queue (push, top, pop, and empty).

Implement the MyStack class:
 - void push(int x) Pushes element x to the top of the stack.
 - int pop() Removes the element on the top of the stack and returns it.
 - int top() Returns the element on the top of the stack.
 - boolean empty() Returns true if the stack is empty, false otherwise.
 
Notes:
  - You must use only standard operations of a queue, which means only push to back, peek/pop from front, 
    size, and is empty operations are valid.
  - Depending on your language, the queue may not be supported natively. 
    You may simulate a queue using a list or deque (double-ended queue), 
    as long as you use only a queue's standard operations.
"""

import collections
class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q = collections.deque()

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.q.append(x)
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return self.q.popleft()

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.q[0]

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return len(self.q) == 0

"""
Submissions:
Runtime: 24 ms, faster than 93.42% of Python3 online submissions for Implement Stack using Queues.
Memory Usage: 14.4 MB, less than 5.11% of Python3 online submissions for Implement Stack using Queues.
"""

myStack=MyStack()
myStack.push(1)
myStack.push(2)
print(myStack.top())
print(myStack.pop())
print(myStack.empty())
