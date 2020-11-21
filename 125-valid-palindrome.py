#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 21 02:59:45 2020

@author: Jack Kim
"""

"""
Problem:
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
Note: For the purpose of this problem, we define empty string as valid palindrome.
"""

class Solution_1:
    def isPalindrome(self, s: str) -> bool:
        word_only=[]
        p_word=[]
        for word in s:
            if word.isalpha() :
                word_only.append(word.lower())
            elif word.isdigit():
                word_only.append(word)
                
        p_word[:]=word_only[::-1]
        
        if word_only == p_word:
            return True
        else:
            return False
"""
Submissions:
Runtime: 52 ms, faster than 41.68% of Python3 online submissions for Valid Palindrome.
Memory Usage: 20.5 MB, less than 5.30% of Python3 online submissions for Valid Palindrome.
"""

class Solution_2:
    def isPalindrome(self, s: str) -> bool:
        strs=[]
        for char in s:
            if char.isalnum():
                strs.append(char.lower())
            
        while len(strs) > 1:
            if strs.pop(0) != strs.pop(): # strs.pop(0) is O(n).
                return False
        return True


"""
Submissions:
Runtime: 284 ms, faster than 5.29% of Python3 online submissions for Valid Palindrome.
Memory Usage: 19.5 MB, less than 11.63% of Python3 online submissions for Valid Palindrome.
"""

import collections
class Solution_3:
    def isPalindrome(self, s: str) -> bool:
        strs:Deque = collections.deque()
            
        for char in s:
            if char.isalnum():
                strs.append(char.lower())
                
        while len(strs) > 1:
            if strs.popleft() != strs.pop(): # strs.popleft is O(1).
                return False
        return True

"""
Submissions:
Runtime: 44 ms, faster than 76.89% of Python3 online submissions for Valid Palindrome.
Memory Usage: 19.3 MB, less than 14.34% of Python3 online submissions for Valid Palindrome.
"""

import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        s=re.sub('[^a-z0-9]', '', s)
        
        return s == s[::-1]

"""
Submissions:
Runtime: 40 ms, faster than 87.87% of Python3 online submissions for Valid Palindrome.
Memory Usage: 15.8 MB, less than 18.86% of Python3 online submissions for Valid Palindrome.
"""


S=Solution()
s="A man, a plan, a canal: Panama"
print(S.isPalindrome(s))