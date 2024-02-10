#!/usr/bin/env python3
"""
@author: Jack Kim
"""

"""
Problems:
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
"""

class Solution:
    def containsDuplicate(self, nums) -> bool:
        nums.sort()

        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return True

        return False
"""
Submissions:
Runtime 445 ms Beats 38.28% of users with Python3
Memory 28.23 MB Beats 97.81% of users with Python3
"""
class Solution2:
    def containsDuplicate(self, nums: List[int]) -> bool:
        for i in set(nums):
            if nums.count(i) > 1:
                return True
        return False

"""
Submissions:
Time Limit Exceeded
"""

class Solution3:
    def containsDuplicate(self, nums: List[int]) -> bool:
        s = set(nums)
        return len(nums)!=len(s)
"""
Submissions:
Runtime 422 ms Beats 69.19% of users with Python3
Memory 31.91 MB Beats 73.05% of users with Python3
"""

class Solution4:
    def containsDuplicate(self, nums: List[int]) -> bool:
        d = defaultdict(int)
        for n in nums:
            d[n] += 1
            if d[n] > 1:
                return True
        return False
"""
Submissions:
Runtime 405 ms Beats 96.22% of users with Python3
Memory 34.73 MB Beats 13.80% of users with Python3
"""

S=Solution()
nums=[1,2,3,1]
print(S.containsDuplicate(nums))
nums=[1,2,3,4]
print(S.containsDuplicate(nums))
nums=[1,1,1,3,3,4,3,2,4,2]
print(S.containsDuplicate(nums))
