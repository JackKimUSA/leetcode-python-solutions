#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 10 21:10:27 2020

@author: Jack Kim
"""

"""
Problems:

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

    1. Open brackets must be closed by the same type of brackets.
    2. Open brackets must be closed in the correct order.
"""


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        table = {
            ')': '(',
            '}': '{',
            ']': '[',
        }

        for char in s:
            if char not in table:
                stack.append(char)
            elif not stack or table[char] != stack.pop():
                return False

        return len(stack) == 0

"""
Submissions:
Runtime: 28 ms, faster than 80.69% of Python3 online submissions for Valid Parentheses.
Memory Usage: 14.1 MB, less than 65.11% of Python3 online submissions for Valid Parentheses.
"""