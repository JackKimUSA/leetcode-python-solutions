# -*- coding: utf-8 -*-
"""
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
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 1: return 1

        p1 = 0
        p2 = 1

        x = 0

        if len(nums) == 2:
            if nums[0] == nums[1]:
                return 1
            else:
                return 2

        for i in range(1, len(nums)):
            if nums[p1] == nums[p2]:
                p2 += 1
            else:
                nums[x+1] = nums[p2]
                p1 = p2
                p2 += 1
                x += 1
        nums[:]=nums[:x+1]

        return len(nums)
"""
Submissions:
Runtime 99 ms   Beats 68.20%    Memory 18 MB    Beats 57.67%
"""


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 1: return 1

        x = 0

        for i in range(1, len(nums)):
            if nums[x] != nums[i]:
                nums[x + 1] = nums[i]
                x += 1

        nums[:] = nums[:x + 1]

        return len(nums)

"""
Submissions:
Runtime 92 ms   Beats 90.21%    Memory 18 MB    Beats 57.67%
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
Runtime 86 ms   Beats 97.72%    Memory 17.9 MB  Beats 91.44%

Runtime: 72 ms, faster than 97.37% of Python3 online submissions for Remove Duplicates from Sorted Array.
Memory Usage: 16 MB, less than 51.92% of Python3 online submissions for Remove Duplicates from Sorted Array.
"""
                
                
S = Solution
nums=[0,0,1,1,1,2,2,3,3,4]
length=S.removeDuplicates(nums)

print(length, nums)