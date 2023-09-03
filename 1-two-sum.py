#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 19:40:14 2020

@author: Jack Kim
"""

"""
Problem:
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

"""

class Solution_1:
    def twoSum(self, nums:int, target:int) -> int:
        res=[]
        for i in range(1,len(nums)):
            key=target - int(nums[i-1])
            for j in range(i,len(nums)):
                if key == nums[j]:
                    res.append(i-1)
                    res.append(j)
                    break
        return res
"""
Submissions:
Runtime: 3532 ms, faster than 27.92% of Python3 online submissions for Two Sum.
Memory Usage: 15 MB, less than 76.56% of Python3 online submissions for Two Sum.
"""

class Solution_2:
    def twoSum(self, nums:int, target:int) -> int:
        dic = {}
        for i,num in enumerate(nums):
            if num in dic:
                return (dic[num],i)
            dic[target-num] = i

"""
Submissions:
Runtime: 48 ms, faster than 77.68% of Python3 online submissions for Two Sum.
Memory Usage: 14.4 MB, less than 100.00% of Python3 online submissions for Two Sum.

"""
# Brute-Force 
class Solution_3:
    def twoSum(self, nums:int, target:int) -> int:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
                
"""
Submisstions:
Runtime: 44 ms, faster than 90.36% of Python3 online submissions for Two Sum.
Memory Usage: 14.4 MB, less than 97.59% of Python3 online submissions for Two Sum.
"""

class Solution_4:
    def twoSum(self, nums:int, target:int) -> int:
        for i , n in enumerate(nums):
            complement = target - n
            if complement in nums[i+1:]:
                return nums.index(n), nums[i+1:].index(complement) + (i+1)
"""
Submissions:
Runtime: 36 ms, faster than 99.36% of Python3 online submissions for Two Sum.
Memory Usage: 14.5 MB, less than 95.86% of Python3 online submissions for Two Sum.
"""

class Solution_5:
    def twoSum(self, nums:int, target:int) -> int:
        nums_map={}
        for i, num in enumerate(nums):
            nums_map[num]=i
        
        for i, num in enumerate(nums):
            if target - num in nums_map and i != nums_map[target - num]:
                return nums.index(num), nums_map[target - num]
            
    
"""
Submissions:
Runtime: 52 ms, faster than 54.62% of Python3 online submissions for Two Sum.
Memory Usage: 14.4 MB, less than 96.48% of Python3 online submissions for Two Sum.
"""
class Solution_6:
    def twoSum(self, nums:int, target:int) -> int:
        nums_map={}
        for i, num in enumerate(nums):
            if target - num in nums_map:
                return [nums_map[target-num], i]
            nums_map[num]=i
            
"""
Submissions:
Runtime: 48 ms, faster than 76.35% of Python3 online submissions for Two Sum.
Memory Usage: 14.4 MB, less than 97.59% of Python3 online submissions for Two Sum.
"""
# Two Point has index issue
#class Solution:
#    def twoSum(self, nums:int, target:int) -> int:
#        nums.sort()
#        left,right = 0, len(nums) - 1
#        while not left == right:
#            if nums[left] + nums[right] < target:
#                left += 1
#            elif nums[left] + nums[right] > target:
#                right -= 1
#            else:
#                return left, right

      
S=Solution()
nums=[2,11,7,15]
target=9
print(S.twoSum(nums, target))

