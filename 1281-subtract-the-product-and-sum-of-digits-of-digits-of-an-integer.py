#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  3 19:59:18 2020

@author: jgkim
"""
"""
Problem:
Given an integer number n, return the difference between the product of its digits and the sum of its digits.
"""

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        pd=1
        for i in str(n):
            pd = pd * int(i)
        s=0
        for j in str(n):
            s = s + int(j)
        return pd - s

n = 234
S=Solution()
print(S.subtractProductAndSum(n))

"""
Submissions:
Runtime: 32 ms, faster than 35.33% of Python3 online submissions for Subtract the Product and Sum of Digits of an Integer.
Memory Usage: 13.6 MB, less than 100.00% of Python3 online submissions for Subtract the Product and Sum of Digits of an Integer.
"""