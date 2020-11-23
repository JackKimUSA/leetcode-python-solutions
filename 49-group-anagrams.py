#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 13:49:05 2020

@author: Jack Kim
"""

"""
Problem:
Given an array of strings strs, group the anagrams together. You can return the answer in any order.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically 
using all the original letters exactly once.
"""

class Solution_1:
    def groupAnagrams(self, strs: str) -> str:
        group_anagrams=[]
        group=[]
        groups=[]
        for i in range(len(strs)):
            if strs[i] not in groups:
                group=[]
                for j in range(len(strs)):
                    if sorted(strs[i]) == sorted(strs[j]):
                        group.append(strs[j])
                groups=groups+group
                group_anagrams.append(group)
        return group_anagrams

"""
Submissions:
Time Limit Exceeded
"""
            
import collections
class Solution:
    def groupAnagrams(self, strs: str) -> str:
        anagrams = collections.defaultdict(list)
            
        for word in strs:
            anagrams[''.join(sorted(word))].append(word)
        return anagrams.values()

"""
Submissions:
Runtime: 100 ms, faster than 49.89% of Python3 online submissions for Group Anagrams.
Memory Usage: 17.7 MB, less than 45.70% of Python3 online submissions for Group Anagrams.
"""

strs=["eat","tea","tan","ate","nat","bat"]
S=Solution()
print(S.groupAnagrams(strs))
