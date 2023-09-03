#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Jack Kim
"""
"""
Problem:
Given an integer array nums containing n integers, find the beauty of each subarray of size k.
The beauty of a subarray is the xth smallest integer in the subarray if it is negative, 
or 0 if there are fewer than x negative integers.

Return an integer array containing n - k + 1 integers, which denote the beauty of the subarrays in order 
from the first index in the array.

A subarray is a contiguous non-empty sequence of elements within an array.

Constraints:
n == nums.length 
1 <= n <= 105
1 <= k <= n
1 <= x <= k 
-50 <= nums[i] <= 50 
"""

class Solution:
    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
        results = []
        for i in range(len(nums) - k + 1):
            sk = sorted(nums[i:i + k])
            if sk[x - 1] > 0:
                results.append(0)
            else:
                results.append(sk[x - 1])

        return results
"""
Submissions:
Time Limit Exceeded
"""

class Solution:
    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
        results = []
        for i in range(len(nums) - k + 1):
            sk = sorted(nums[i:i + k])[x - 1]
            if sk > 0:
                results.append(0)
            else:
                results.append(sk)

        return results
"""
Submissions:
Time Limit Exceeded
"""

class Solution:
    def findKthSmallest(self, nums: List[int], x: int) -> int:
        heap = list()

        for n in nums:
            heapq.heappush(heap, n)

        for _ in range(1, x):
            heapq.heappop(heap)

        return heapq.heappop(heap)

    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
        results = []
        for i in range(len(nums) - k + 1):
            sk = self.findKthSmallest(nums[i:i + k], x)
            if sk > 0:
                results.append(0)
            else:
                results.append(sk)

        return results
"""
Submissions:
Time Limit Exceeded
"""


class Solution:
    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
        results = []
        for i in range(len(nums) - k + 1):
            sk = heapq.nsmallest(x, nums[i:i + k])[-1]
            if sk > 0:
                results.append(0)
            else:
                results.append(sk)

        return results
"""
Submissions:
Time Limit Exceeded
"""

from sortedcontainers import SortedList

class Solution:
    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
        ans = []
        vals = SortedList()
        for i, v in enumerate(nums):
            vals.add(v)
            if i >= k:
                vals.remove(nums[i-k])
            if i >= k-1:
                ans.append(min(0, vals[x-1]))
        return ans
"""
Submissions:
Runtime 6083ms  Beats 46.66%    Memory 31.3MB  Beats 27.71%
"""