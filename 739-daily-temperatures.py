#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 21:10:27 2020

@author: Jack Kim
"""

"""
Problems:
Given a list of daily temperatures T, return a list such that, for each day in the input, 
tells you how many days you would have to wait until a warmer temperature. 
If there is no future day for which this is possible, put 0 instead.

For example, given the list of temperatures T = [73, 74, 75, 71, 69, 72, 76, 73], 
your output should be [1, 1, 4, 2, 1, 1, 0, 0].

Note: The length of temperatures will be in the range [1, 30000]. 
Each temperature will be an integer in the range [30, 100].
"""

class Solution:
    def dailyTemperatures(self, T):
        answer = [0] * len(T)
        stack=[]
        for i, cur in enumerate(T):
            while stack and cur > T[stack[-1]]:
                last = stack.pop()
                answer[last] = i - last
            stack.append(i)
            print(stack)
        return answer

"""
Submissions:
Runtime: 488 ms, faster than 88.88% of Python3 online submissions for Daily Temperatures.
Memory Usage: 18.9 MB, less than 25.45% of Python3 online submissions for Daily Temperatures.
"""
T=[73, 74, 75, 71, 69, 72, 76, 73]
S=Solution()
print(S.dailyTemperatures(T))

