#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 22:28:43 2020

@author: Jack Kim
"""
"""
Problems:
Given a non-empty array of integers, return the k most frequent elements.
"""
import collections
import heapq

class Solution_1:
    def topKFrequent(self, nums, k: int):
        freqs=collections.Counter(nums)
        freqs_heap=list()
        for f in freqs:
            heapq.heappush(freqs_heap, (-freqs[f], f))
        topk = []
        for _ in range(k):
            topk.append(heapq.heappop(freqs_heap)[1])
        return topk
        
"""
Submissions:
Runtime: 104 ms, faster than 40.69% of Python3 online submissions for Top K Frequent Elements.
Memory Usage: 18.7 MB, less than 43.85% of Python3 online submissions for Top K Frequent Elements.
"""

class Solution:
    def topKFrequent(self, nums, k: int):
        return list(zip(*collections.Counter(nums).most_common(k)))[0]
"""
Submissions:
Runtime: 96 ms, faster than 82.16% of Python3 online submissions for Top K Frequent Elements.
Memory Usage: 18.5 MB, less than 54.35% of Python3 online submissions for Top K Frequent Elements.
"""
nums=[1,1,1,2,2,3]
k=2
S=Solution()
print(S.topKFrequent(nums,k))
        