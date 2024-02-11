#!/usr/bin/env python3
"""
@author: Jack Kim
"""

"""
Problems:
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
typically using all the original letters exactly once.
"""


class Solution1:
    def isAnagram(self, s: str, t: str) -> bool:
        ls = list(s)
        lt = list(t)
        ls.sort()
        lt.sort()
        if ls == lt:
            return True
        return False

"""
Submissions:
Runtime 55 ms Beats 39.82% of users with Python3
Memory 17.49 MB Beats 50.67% of users with Python3
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        if sorted(s) == sorted(t):
            return True
        return False

"""
Submissions:
Runtime 55 ms Beats 39.82% of users with Python3
Memory 17.28 MB Beats 56.40% of users with Python3
"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

"""
Submissions:
Runtime 47 ms Beats 74.85% of users with Python3
Memory 17.42 MB Beats 50.67% of users with Python3
"""

from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_map = defaultdict(int)
        t_map = defaultdict(int)
        for a in s:
            s_map[a] += 1
        for a in t:
            t_map[a] += 1

        if s_map == t_map:
            return True
        return False

"""
Submissions
Runtime 50 ms Beats 62.00% of users with Python3
Memory 16.98 MB Beats 68.87% of users with Python3
"""


S = Solution()
s = "anagram"
t = "nagaram"
print(S.isAnagram(s, t))
s = "rat"
t = "car"
print(S.isAnagram(s, t))
