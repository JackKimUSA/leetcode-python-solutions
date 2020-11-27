#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 07:44:12 2020

@author: Jack Kim
"""

"""
Problem:
Given an array nums of n integers where n > 1,  return an array output 
such that output[i] is equal to the product of all the elements of nums except nums[i].
"""

class Solution:
    def productExceptSelf(self, nums: int) -> int:
        out = []
        p = 1
        for i in range(0, len(nums)):
            out.append(p)ß
            p = p * nums[i]
        
        p = 1
        for i in range(len(nums) - 1, 0 - 1, -1):
            out[i]=out[i]*p
            p=p*nums[i]
        return out

"""
Submissions:
Runtime: 224 ms, faster than 70.38% of Python3 online submissions for Product of Array Except Self.
Memory Usage: 21 MB, less than 57.73% of Python3 online submissions for Product of Array Except Self.
"""

nums=[1,2,3,4]
S=Solution()
print(S.productExceptSelf(nums))