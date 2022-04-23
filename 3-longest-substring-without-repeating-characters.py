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
class Solution1:
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

# Brute Force : TC O(n^3), SC O(k)
class Solution2:
    def lengthOfLongestSubstring(s: str) -> int:
        def check(start, end):
            chars = [0] * 128
            for i in range(start, end + 1):
                c = s[i]
                chars[ord(c)] += 1
                if chars[ord(c)] > 1:
                    return False
            return True

        n = len(s)

        res = 0
        for i in range(n):
            for j in range(i, n):
                if check(i, j):
                    res = max(res, j - i + 1)
        return res

"""
Submissions:
Time Limit Exceeded
"""

# Sliding Window : TC O(n), SC O(k)
class Solution3:
    def lengthOfLongestSubstring(s: str) -> int:
        chars = [0] * 128

        left = right = 0

        res = 0
        while right < len(s):
            r = s[right]
            chars[ord(r)] += 1

            while chars[ord(r)] > 1:
                l = s[left]
                chars[ord(l)] -= 1
                left += 1

            res = max(res, right - left + 1)

            right += 1
        return res
"""
Submissions:
Runtime: 96 ms, faster than 49.20% of Python3 online submissions for Longest Substring Without Repeating Characters.
Memory Usage: 14.1 MB, less than 52.58% of Python3 online submissions for Longest Substring Without Repeating Characters.
"""

# Sliding Window Optimized : TC O(n), SC O(m)
class Solution:
    def lengthOfLongestSubstring(s: str) -> int:
        n = len(s)
        ans = 0
        # mp stores the current index of a character
        mp = {}

        i = 0
        # try to extend the range [i, j]
        for j in range(n):
            if s[j] in mp:
                i = max(mp[s[j]], i)

            ans = max(ans, j - i + 1)
            mp[s[j]] = j + 1

        return ans

"""
Submissions:
Runtime: 82 ms, faster than 63.16% of Python3 online submissions for Longest Substring Without Repeating Characters.
Memory Usage: 14 MB, less than 52.58% of Python3 online submissions for Longest Substring Without Repeating Characters
"""

s = "abcabcbb"
S = Solution

print(S.lengthOfLongestSubstring(s))

