#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  3 19:45:03 2020

@author: jgkim
"""

"""
Problem:
Given a non-negative integer num, return the number of steps to reduce it to zero. If the current number is even, you have to divide it by 2, otherwise, you have to subtract 1 from it.
"""

class Solution:
    def numberOfSteps (self, num: int) -> int:
        oNum = num
        sNum = 0
        while oNum != 0:
            if oNum % 2 == 0:
                oNum = oNum /2
                sNum = sNum + 1
            else:
                oNum = oNum -1
                sNum = sNum + 1
        return sNum

num = 14
S=Solution()
print(S.numberOfSteps(num))

"""
Submissions:
Runtime: 28 ms, faster than 70.49% of Python3 online submissions for Number of Steps to Reduce a Number to Zero.
"""