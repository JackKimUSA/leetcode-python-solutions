#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Sun Nov 10 03:09:20 2019

@author: Jack Kim
"""

"""
Problem:
Implement function ToLowerCase() that has a string parameter str, and returns 
the same string in lowercase.

"""

class Solution(object):
    def toLowerCase(self, str):
        return str.lower()

S=Solution()
print(S.toLowerCase("Hello"))

"""
Submissions:
Runtime: 16 ms, faster than 66.21% of Python online submissions for To Lower Case.
Memory Usage: 11.8 MB, less than 24.14% of Python online submissions for To Lower Case.
"""

