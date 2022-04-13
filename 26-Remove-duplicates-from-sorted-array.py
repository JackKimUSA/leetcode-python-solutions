# -*- coding: utf-8 -*-
"""
Created on Wed May  5 02:25:13 2021

@author: Jack Kim
"""

"""
Problem:
Given a sorted array nums, remove the duplicates in-place such that each element appears only once and 
returns the new length.
Do not allocate extra space for another array, you must do this by modifying the input array in-place 
with O(1) extra memory.
"""

class Solution:
    def removeDuplicates(nums):
        if len(nums) == 0 : return 0
        if len(nums) == 1 : return 1
        
        x = 1
        
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[x] = nums[i]
                x += 1
        
        nums[:]=nums[:x]
        
        return x

"""
Submissions:
Runtime: 72 ms, faster than 97.37% of Python3 online submissions for Remove Duplicates from Sorted Array.
Memory Usage: 16 MB, less than 51.92% of Python3 online submissions for Remove Duplicates from Sorted Array.
"""
                
                
S = Solution
nums=[0,0,1,1,1,2,2,3,3,4]
length=S.removeDuplicates(nums)

print(length, nums)