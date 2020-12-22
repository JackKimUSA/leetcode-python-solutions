#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 05:00:19 2020

@author: Jack Kim
"""

"""
Problems:
Design a HashMap without using any built-in hash table libraries.

To be specific, your design should include these functions:

  - put(key, value) : Insert a (key, value) pair into the HashMap. 
    If the value already exists in the HashMap, update the value.
  - get(key): Returns the value to which the specified key is mapped,
    or -1 if this map contains no mapping for the key.
  - remove(key) : Remove the mapping for the value key if this map 
    contains the mapping for the key.
"""

# Separate Chaining

import collections

class ListNode:
    def __init__(self, key=None, value=None):
        self.key=key
        self.value=value
        self.next=None
        
class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 1000
        self.table = collections.defaultdict(ListNode)

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        index = key % self.size
        if self.table[index].value is None: 
            self.table[index] = ListNode(key,value)
            return
        
        p = self.table[index]
        while p:
            if p.key == key:
                p.value = value
                return
            if p.next is None:
                break
            p=p.next
        p.next = ListNode(key,value)

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        index = key % self.size
        if self.table[index].value is None:
            return -1
        
        p = self.table[index]
        while p:
            if p.key == key:
                return p.value
            p = p.next
        return -1

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        index = key % self.size
        if self.table[index].value is None:
            return
        
        p = self.table[index]
        if p.key == key:
            self.table[index] = ListNode() if p.next is None else p.next
            return
        
        prev = p
        while p:
            if p.key == key:
                prev.next = p.next
                return
            prev, p = p, p.next
"""
Submissions:
Runtime: 232 ms, faster than 54.93% of Python3 online submissions for Design HashMap.
Memory Usage: 17.5 MB, less than 43.90% of Python3 online submissions for Design HashMap.
"""

myhash=MyHashMap()
myhash.put(1,1)
myhash.put(2,2)
print(myhash.get(1))
print(myhash.get(3))
myhash.put(2,1)
print(myhash.get(2))
myhash.remove(2)
print(myhash.get(2))




