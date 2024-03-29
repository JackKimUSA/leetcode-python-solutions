#!/usr/bin/env python3
"""
@author: Jack Kim
"""

"""
Problems:
There are n buildings in a line. You are given an integer array heights of size n that represents the heights of the buildings in the line.
The ocean is to the right of the buildings. A building has an ocean view if the building can see the ocean without obstructions. 
Formally, a building has an ocean view if all the buildings to its right have a smaller height.
Return a list of indices (0-indexed) of buildings that have an ocean view, sorted in increasing order.
"""

import math
class Solution:
    def findBuildings(self, heights):
        res = []
        max = -math.inf

        for i in range(len(heights) - 1, -1, -1):
            if max < heights[i]:
                max = heights[i]
                res.append(i)

        return res[::-1]

"""
Submissions:
Runtime 490 ms Beats 83.78% of users with Python3
Memory 34.06 MB Beats 65.11% of users with Python3
"""
S=Solution()
heights=[4,2,3,1]
print(S.findBuildings(heights))

heights=[4,3,2,1]
print(S.findBuildings(heights))

heights=[1,3,2,4]
print(S.findBuildings(heights))
