#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Jack Kim
"""

"""
Problem:
You are given a sorted array consisting of only integers where every element appears exactly twice, 
except for one element which appears exactly once.
Return the single element that appears only once.
Your solution must run in O(log n) time and O(1) space.
"""


class Solution:
    def singleNonDuplicate(self, nums):
        left, right = 0, len(nums) - 1

        while (left < right):
            mid = left + (right - left)//2

            if mid & 1:
                mid -= 1

            if nums[mid] == nums[mid+1]:
                left = mid + 2
            else:
                right = mid

        return nums[left]


"""
Submissions:
Runtime 139 ms Beats 76.78% of users with Python3
Memory 26.60 MB Beats 79.11% of users with Python3  
"""

S = Solution()
nums = [1, 1, 2, 3, 3, 4, 4, 8, 8]
print(S.singleNonDuplicate(nums))

nums = [3, 3, 7, 7, 10, 11, 11]
print(S.singleNonDuplicate(nums))
