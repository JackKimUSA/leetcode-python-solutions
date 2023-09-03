#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Jack Kim
"""

"""
Problem:
Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.Ï

Can you solve it without sorting?

Constraints:

1 <= k <= nums.length <= 10^5
-10^4 <= nums[i] <= 10^4
"""

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort(reverse=True)
        return nums[k - 1]

"""
Submissions:
Runtime 500 ms  Beats 80.16%    Memory 29.6 MB  Beats 58.18%
"""

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap)

        return heap[0]

"""
Submissions:
Runtime 573 ms  Beats 32.85%    Memory 29.9 MB  Beats 38.8%
"""


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def quick_select(nums, k):
            pivot = random.choice(nums)
            left, mid, right = [], [], []

            for num in nums:
                if num > pivot:
                    left.append(num)
                elif num < pivot:
                    right.append(num)
                else:
                    mid.append(num)

            if k <= len(left):
                return quick_select(left, k)

            if len(left) + len(mid) < k:
                return quick_select(right, k - len(left) - len(mid))

            return pivot

        return quick_select(nums, k)
"""
Submissions:
Runtime 508 ms  Beats 76.80%    Memory 30.2 MB  Beats 27.28%
"""


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_value = min(nums)
        max_value = max(nums)

        count = [0] * (max_value - min_value + 1)

        for num in nums:
            count[num - min_value] += 1

        remain = k

        for num in range(len(count) - 1, -1, -1):
            remain -= count[num]
            if remain <= 0:
                return num + min_value

        return -1

"""
Submissions:
Runtime 487 ms  Beats 87.59%    Memory 29.5 MB  Beats 81%
"""