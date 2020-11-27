#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 01:57:29 2020

@author: Jack Kim
"""
class Node:
    def __init__ (self, data=None):
        self.data=data
        self.next=None
        
n1 = Node('eggs')
n2 = Node('ham')
n3 = Node('spam')

n1.next = n2
n2.next = n3

current = n1
while current:
    print(current.data)
    current = current.next

# Singly Linked List Class
class SinglyLinkedList:
    def __int__ (self):
        self.tail = None
    
    def append(self, data):
        node = Node(data)
        if self.tail == None:
            self.tail = node
        else:
            current = self.tail
            while current.next:
                current = current.next
            current.next = node

words = SinglyLinkedList()
words.append('egg')
words.append('ham')
words.append('spam')