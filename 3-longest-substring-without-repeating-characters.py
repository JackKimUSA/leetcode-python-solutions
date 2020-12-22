#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 20:32:10 2020

@author: Jack Kim
"""
"""
Problems:
Given a string s, find the length of the longest substring without repeating characters.
"""

# Two Pointers
class Solution:
    def lengthOfLongestSubstring(s: str) -> int:
        used={}
        max_length = start = 0
        
        for index, char in enumerate(s):
            if char in used and start <= used[char]:
                start=used[char] + 1
            else:
                max_length = max(max_length, index - start + 1)
            used[char] = index
        return max_length
    
"""
Submissions:
Runtime: 48 ms, faster than 95.43% of Python3 online submissions for Longest Substring Without Repeating Characters.
Memory Usage: 14.2 MB, less than 90.07% of Python3 online submissions for Longest Substring Without Repeating Characters.
"""

s = "abcabcbb"
S = Solution

print(S.lengthOfLongestSubstring(s))