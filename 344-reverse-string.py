#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 21 03:53:17 2020

@author: Jack Kim
"""

"""
Problem:
Write a function that reverses a string. The input string is given as an array of characters char[].

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

You may assume all the characters consist of printable ascii characters.
"""

class Solution_1:
    def reverseString(self, s: str) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s[:]=s[::-1]
"""
Submissions:
Runtime: 180 ms, faster than 98.98% of Python3 online submissions for Reverse String.
Memory Usage: 18.7 MB, less than 9.31% of Python3 online submissions for Reverse String.
"""      

class Solution_2:
    def reverseString(self, s: str) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s.reverse()
"""
Submissions:
Runtime: 196 ms, faster than 65.34% of Python3 online submissions for Reverse String.
Memory Usage: 18.5 MB, less than 46.76% of Python3 online submissions for Reverse String.
"""      
 
class Solution:
    def reverseString(self, s: str) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left, right = 0, len(s) - 1
        while left < right:
            s[left],s[right] = s[right], s[left]
            left += 1
            right -= 1

"""
Submissions:
Runtime: 188 ms, faster than 91.08% of Python3 online submissions for Reverse String.
Memory Usage: 18.5 MB, less than 46.76% of Python3 online submissions for Reverse String.
"""        

s=["h","e","l","l","o"]
S=Solution();
S.reverseString(s)
print(s)

