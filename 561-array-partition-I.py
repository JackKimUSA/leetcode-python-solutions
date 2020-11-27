#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 07:17:19 2020

@author: Jack Kim
"""

"""
Problem:
Given an integer array nums of 2n integers, group these integers into n pairs (a1, b1), (a2, b2), ..., (an, bn) 
such that the sum of min(ai, bi) for all i is maximized. Return the maximized sum.
"""
class Solution_1:
    def arrayPairSum(self, nums: int) -> int:
        sum = 0
        pair=[]
        nums.sort()
        
        for n in nums:
            pair.append(n)
            if len(pair) == 2:
                sum += min(pair)
                pair=[]
        return sum
"""
Submissions:
Runtime: 280 ms, faster than 16.35% of Python3 online submissions for Array Partition I.
Memory Usage: 16.9 MB, less than 34.38% of Python3 online submissions for Array Partition I.
"""
   
class Solution_2:
    def arrayPairSum(self, nums: int) -> int:
        sum=0
        nums.sort()
        
        for i, n in enumerate(nums):
            if i % 2 == 0:
                sum +=n
        return sum
"""
Submissions:
Runtime: 280 ms, faster than 16.35% of Python3 online submissions for Array Partition I.
Memory Usage: 16.9 MB, less than 5.81% of Python3 online submissions for Array Partition I.
"""
class Solution:
    def arrayPairSum(self, nums: int) -> int:
        return sum(sorted(nums)[::2])
"""
Submissions:
Runtime: 260 ms, faster than 59.35% of Python3 online submissions for Array Partition I.
Memory Usage: 16.9 MB, less than 5.81% of Python3 online submissions for Array Partition I.
"""
nums=[1,4,3,2]
S=Solution()
print(S.arrayPairSum(nums))