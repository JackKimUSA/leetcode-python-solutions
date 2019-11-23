#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 22:45:55 2019

@author: Jack Kim
"""

"""
You're given strings J representing the types of stones that are jewels, and S representing the stones you have.
Each character in S is a type of stone you have.  You want to know how many of the stones you have are also jewels.

The letters in J are guaranteed distinct, and all characters in J and S are letters. Letters are case sensitive, 
so "a" is considered a different type of stone from "A".
"""

class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        count=0
        for j in J:
            count += S.count(j)
        return count

J="aA"
S="aAAbbbb"
Sol=Solution()
print(Sol.numJewelsInStones(J,S))

"""
Submissions:
Runtime: 28 ms, faster than 94.82% of Python3 online submissions for Jewels and Stones.
Memory Usage: 12.6 MB, less than 100.00% of Python3 online submissions for Jewels and Stones.
"""
