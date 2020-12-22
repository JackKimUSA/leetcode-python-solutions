#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 22:45:55 2019

@author: Jack Kim
"""

"""
Problems:
You're given strings jewels representing the types of stones that are jewels, 
and stones representing the stones you have. Each character in stones is a type of stone you have. 
You want to know how many of the stones you have are also jewels.

Letters are case sensitive, so "a" is considered a different type of stone from "A".
"""

class Solution_1:
    def numJewelsInStones(self, J: str, S: str) -> int:
        count=0
        for j in J:
            count += S.count(j)
        return count
"""
Submissions:
Runtime: 28 ms, faster than 94.82% of Python3 online submissions for Jewels and Stones.
Memory Usage: 12.6 MB, less than 100.00% of Python3 online submissions for Jewels and Stones.
"""

class Solution_2:
    def numJewelsInStones(self, J: str, S: str) -> int:
        return len([i for i in S if i in J])
"""
Submissions:
Runtime: 20 ms, faster than 98.79% of Python3 online submissions for Jewels and Stones.
Memory Usage: 14.3 MB, less than 27.09% of Python3 online submissions for Jewels and Stones]
"""

# Hash Table
class Solution_3:
    def numJewelsInStones(self, J: str, S: str) -> int:
        freqs = {}
        
        for char in S:
            if char not in freqs:
                freqs[char] = 1
            else:
                freqs[char] += 1
        
        count = 0
        for char in J:
            if char in freqs:
                count += freqs[char]
        return count
"""
Submissions:
Runtime: 28 ms, faster than 80.76% of Python3 online submissions for Jewels and Stones.
Memory Usage: 14.3 MB, less than 27.09% of Python3 online submissions for Jewels and Stones.
"""

# defaultdict
import collections
class Solution_4:
    def numJewelsInStones(self, J: str, S: str) -> int:
        freqs=collections.defaultdict(int)
        count = 0
        
        for char in S:
            freqs[char] += 1
        
        for char in J:
            count += freqs[char]
        return count

"""
Submissions:
Runtime: 32 ms, faster than 55.03% of Python3 online submissions for Jewels and Stones.
Memory Usage: 14.3 MB, less than 27.09% of Python3 online submissions for Jewels and Stones.
"""

# Counter
class Solution_5:
    def numJewelsInStones(self, J: str, S: str) -> int:
        freqs=collections.Counter(S)
        count = 0
        for char in J:
            count += freqs[char]
        return count
"""
Submissions:
Runtime: 28 ms, faster than 80.76% of Python3 online submissions for Jewels and Stones.
Memory Usage: 14.3 MB, less than 27.09% of Python3 online submissions for Jewels and Stones.
"""

# List Comprehensions
class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        return sum(s in J for s in S)

J="aA"
S="aAAbbbb"
Sol=Solution()
print(Sol.numJewelsInStones(J,S))


