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

class Solution_1:
    def removeDuplicateLetters(self, s: str) -> str:
        for char in sorted(set(s)):
            suffix = s[s.index(char):]
            if set(s) == set(suffix):
                return char + self.removeDuplicateLetters(suffix.replace(char,''))
        return ''

"""
Submissions:
Runtime: 52 ms, faster than 13.57% of Python3 online submissions for Remove Duplicate Letters.
Memory Usage: 14.6 MB, less than 5.12% of Python3 online submissions for Remove Duplicate Letters.
"""
import collections
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        counter, seen, stack = collections.Counter(s), set(), []

        for char in s:
            counter[char] -= 1
            if char in seen:
                continue

            while stack and char < stack[-1] and counter[stack[-1]] > 0:
                seen.remove(stack.pop())
            stack.append(char)
            seen.add(char)

        return ''.join(stack)

"""
Submissions
Runtime: 36 ms, faster than 69.37% of Python3 online submissions for Remove Duplicate Letters.
Memory Usage: 14.4 MB, less than 12.45% of Python3 online submissions for Remove Duplicate Letters.
"""

s="cbacdcbc"
S=Solution()
print(S.removeDuplicateLetters(s))