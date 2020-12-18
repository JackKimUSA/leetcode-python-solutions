#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 10 21:10:27 2020

@author: Jack Kim
"""

"""
Problems:

Given a string s, remove duplicate letters so that every letter appears once and only once. 
You must make sure your result is the smallest in lexicographical order among all possible results.

Note: This question is the same as 1081: https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/
"""

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        print(sorted(set(s)))
        for char in sorted(set(s)):
            suffix = s[s.index(char):]
            print(suffix)
            if set(s) == set(suffix):
                return char + self.removeDuplicateLetters(suffix.replace(char,''))
        return ''

"""
Submisstions:
Runtime: 52 ms, faster than 13.57% of Python3 online submissions for Remove Duplicate Letters.
Memory Usage: 14.6 MB, less than 5.12% of Python3 online submissions for Remove Duplicate Letters.
"""

s="cbacdcbc"
S=Solution()
print(S.removeDuplicateLetters(s))