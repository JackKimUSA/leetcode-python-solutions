#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 05:39:15 2020

@author: Jack Kim
"""

"""
Problem:
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? 
Find all unique triplets in the array which gives the sum of zero.

Notice that the solution set must not contain duplicate triplets.
"""

# Brute-Force has "Time Limit Exceeded"
class Solution_1:
    def threeSum(self, nums: int) -> int:
        results = []
        nums.sort()
        
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-2]:
                continue
            for j in range(i+1, len(nums) -1):
                if j > i + 1 and nums[j] == nums[j-1]:
                    continue
                for k in range(j + 1, len(nums)):
                    if k > j + 1 and nums[k] == nums[k-1]:
                        continue
                    if nums[i] + nums[j] + nums[k] == 0:
                        results.append((nums[i], nums[j], nums[k]))
        return results


# Two Point / Failed nums=[1,-1,-1,0] / Output [] / Expected [[-1,0,1]]
class Solution_2:
    def threeSum(self, nums: int) -> int:
        results = []
        nums.sort()
        
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left,right=i+1, len(nums) -1
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if sum < 0 :
                    left += 1
                elif sum > 0 :
                    right -= 1
                else:
                    results.append((nums[i],nums[left], nums[right]))
                while left < right and nums[left] == nums[left+1]:
                    left += 1
                while left < right and nums[right] == nums[right-1]:
                    right -= 1
                left += 1
                right -= 1
        return results     


class Solution:
    def threeSum(self, nums: int) -> int:
        triplets = []
        nums.sort()
        
        for i in range(len(nums)-2):
### 'cur' - first num in possible triplet
### 'seen' - to keep track of 2sums
### 'used' - to keep track of nums used
            cur, seen, used = nums[i], {}, set()
### Can't get a triplet if the smallest number is postive
            if cur > 0: break
### Ignore numbers that were just looked through
            if i > 0 and cur == nums[i-1]: continue
            for j in range(i+1, len(nums)):
### Only a valid triplet if it is in seen and has not yet been used
                if nums[j] in seen and nums[j] not in used:
                    triplets.append([cur,seen[nums[j]],nums[j]])
                    used.add(nums[j])
                else:
### Record 2sum in 'seen'
                    seen[-(cur+nums[j])] = nums[j]
        return triplets
"""
Submissions:
Runtime: 740 ms, faster than 80.79% of Python3 online submissions for 3Sum.
Memory Usage: 17.6 MB, less than 30.72% of Python3 online submissions for 3Sum.
"""
#nums=[-1,0,1,2,-1,-4]
#nums=[1,-1,-1,0]
#nums=[-1,0,1,0]
nums=[3,0,-2,-1,1,2]
S = Solution()
print(S.threeSum(nums))

