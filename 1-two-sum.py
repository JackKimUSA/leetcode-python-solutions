#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 19:40:14 2020

@author: Jack Kim
"""

"""
Problem:
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

"""

class Solution:
    def twoSum(self, nums:int, target:int) -> int:
        dic = {}
        for i,num in enumerate(nums):
            if num in dic:
                return (dic[num],i)
            dic[target-num] = i

S=Solution()
nums=[2,11,7,15]
target=9
print(S.twoSum(nums, target))

"""
Submissions:
Runtime: 48 ms, faster than 77.68% of Python3 online submissions for Two Sum.
Memory Usage: 14.4 MB, less than 100.00% of Python3 online submissions for Two Sum.

"""
