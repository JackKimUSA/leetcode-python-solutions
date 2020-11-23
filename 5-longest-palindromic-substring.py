#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 20:20:24 2020

@author: Jack Kim
"""

"""
Problem:
Given a string s, return the longest palindromic substring in s.
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(left:int, right:int) -> str:
            while left >=0 and right <=len(s) and s[left] == s[right -1]:
                left -= 1
                right += 1
            return s[left+1:right-1]
        
        if len(s) < 2 or s == s[::-1]:
            return s
        
        result = ''
        for i in range(0,len(s) - 1):
            result=max(result,
                       expand(i,i+1),
                       expand(i,i+2),
                       key=len)
        return result
            
s="babad"
S=Solution()
print(S.longestPalindrome(s))

"""
Submissions:
Runtime: 268 ms, faster than 93.29% of Python3 online submissions for Longest Palindromic Substring.
Memory Usage: 14.3 MB, less than 32.20% of Python3 online submissions for Longest Palindromic Substring.
"""
