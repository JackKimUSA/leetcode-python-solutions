#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 04:44:06 2020

@author: Jack Kim
"""

"""
Problem:
Given n non-negative integers representing an elevation map where the width of each bar is 1, 
compute how much water it can trap after raining.
"""
# Two Point
class Solution_1:
    def trap(self, height: int) -> int:
        if not height:
            return 0
        
        volume = 0
        left,right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]
        
        while left < right:
            left_max, right_max = max(height[left], left_max), max(height[right], right_max)
            
            if left_max <= right_max:
                volume += left_max - height[left]
                left += 1
            else:
                volume += right_max - height[right]
                right -= 1
        return volume
    
"""
Submissions:
Runtime: 56 ms, faster than 42.48% of Python3 online submissions for Trapping Rain Water.
Memory Usage: 14.9 MB, less than 23.05% of Python3 online submissions for Trapping Rain Water.
"""

# Stack
class Solution:
    def trap(self, height: int) -> int:
        stack=[]
        volume = 0
        
        for i in range(len(height)):
            while stack and height[i] > height[stack[-1]]:
                top=stack.pop()
                
                if not len(stack):
                    break
                
                distance = i - stack[-1] - 1
                waters = min(height[i], height[stack[-1]]) - height[top]
                volume += distance * waters
            stack.append(i)
        return volume
    
"""
Submissions:
Runtime: 52 ms, faster than 66.65% of Python3 online submissions for Trapping Rain Water.
Memory Usage: 14.9 MB, less than 23.05% of Python3 online submissions for Trapping Rain Water.
"""
height=[0,1,0,2,1,0,1,3,2,1,2,1]
S=Solution()
print(S.trap(height))