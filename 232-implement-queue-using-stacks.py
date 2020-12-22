#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 21:10:27 2020

@author: Jack Kim
"""

"""
Problems:
Implement a first in first out (FIFO) queue using only two stacks. 
The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).

Implement the MyQueue class:
  - void push(int x) Pushes element x to the back of the queue.
  - int pop() Removes the element from the front of the queue and returns it.
  - int peek() Returns the element at the front of the queue.
  - boolean empty() Returns true if the queue is empty, false otherwise.
  
Notes:
  - You must use only standard operations of a stack, which means only push to top, 
    peek/pop from top, size, and is empty operations are valid.
  - Depending on your language, the stack may not be supported natively. 
    You may simulate a stack using a list or deque (double-ended queue) as long as you use only 
    a stack's standard operations.
"""

class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.input=[]
        self.output=[]

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.input.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        self.peek()
        return self.output.pop()


    def peek(self) -> int:
        """
        Get the front element.
        """
        if not self.output:
            while self.input:
                self.output.append(self.input.pop())
        return self.output[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return self.input == [] and self.output == []

"""
Submissions:
Runtime: 28 ms, faster than 76.65% of Python3 online submissions for Implement Queue using Stacks.
Memory Usage: 14.4 MB, less than 21.28% of Python3 online submissions for Implement Queue using Stacks.
"""

myQueue=MyQueue()
myQueue.push(1)
myQueue.push(2)
print(myQueue.input)
print(myQueue.peek())
print(myQueue.pop())
print(myQueue.empty())
