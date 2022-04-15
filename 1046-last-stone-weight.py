#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 01:51:31 2022

@author: junggyumkim
"""

"""
Problem:
You are given an array of integers stones where stones[i] is the weight of the ith stone.

We are playing a game with the stones. On each turn, we choose the heaviest two stones and 
smash them together. Suppose the heaviest two stones have weights x and y with x <= y. 
The result of this smash is:

If x == y, both stones are destroyed, and
If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.

At the end of the game, there is at most one stone left.

Return the smallest possible weight of the left stone. If there are no stones left, return 0.
    
"""
import heapq

class Solution:
    def lastStoneWeight(self, stones) -> int:
        for i in range(len(stones)):
            stones[i] *= -1
        
        heapq.heapify(stones)
        
        while len(stones) > 1:
            stone1=heapq.heappop(stones)
            stone2=heapq.heappop(stones)
            
            if stone1 != stone2:
                heapq.heappush(stones,(stone1-stone2))
            
        return -heapq.heappop(stones) if stones else 0

stones=[2,7,4,1,8,1]
S=Solution()
print(S.lastStoneWeight(stones))
"""
Submissions:
Runtime: 28 ms, faster than 96.66% of Python3 online submissions for Last Stone Weight.
Memory Usage: 13.9 MB, less than 17.99% of Python3 online submissions for Last Stone Weight.
"""