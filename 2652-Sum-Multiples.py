#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Jack Kim
"""
"""
Problem:
Given a positive integer n, find the sum of all integers in the range [1, n] inclusive that are divisible by 3, 5, or 7.

Return an integer denoting the sum of all numbers in the given range satisfying the constraint.

Constraints:
1 <= n <= 10^3
"""

class Solution1:
    def sumOfMultiples(self, n: int) -> int:
        sum = 0
        for i in range(1, n + 1):
            if i % 3 == 0:
                sum += i
            elif i % 5 == 0:
                sum += i
            elif i % 7 == 0:
                sum += i
        return sum

"""
Submissions:
Runtime 111ms    Beats 10.83%   Memory 16.2MB  Beats 32.20%
"""

class Solution:
    def sumOfMultiples(self, n: int) -> int:
        sum = 0
        for i in range(1, n + 1):
            if i % 3 == 0 or i % 5 == 0 or i % 7 == 0:
                sum += i
        return sum

"""
Submissions:
Runtime 92ms    Beats 51.86%   Memory 16.2MB  Beats 32.20%
"""

S=Solution()
print(S.sumOfMultiples((7)))
print(S.sumOfMultiples((10)))
print(S.sumOfMultiples((9)))