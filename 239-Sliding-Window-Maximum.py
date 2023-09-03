#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Jack Kim
"""
"""
Problem:
You are given an array of integers nums, there is a sliding window of size k which is moving from the very 
left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window 
moves right by one position.

Return the max sliding window.

Constraints:
1 <= nums.length <= 10^5
-10^4 <= nums[i] <= 10^4
1 <= k <= nums.length
"""


class Solution1:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return nums

        r = []
        for i in range(len(nums) - k + 1):
            r.append(max(nums[i:i + k]))
        return r
"""
Submissions:
Time Limit Exceeded
"""

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        results = []
        window = collections.deque()
        float_inf = float('-inf')
        current_max = float_inf
        for i, v in enumerate(nums):
            window.append(v)
            if i < k - 1:
                continue

            if current_max == float_inf:
                current_max = max(window)
            elif v > current_max:
                current_max = v

            results.append(current_max)

            if current_max == window.popleft():
                current_max = float_inf

        return results

    """
    Submissions:
    Time Limit Exceeded
    """

