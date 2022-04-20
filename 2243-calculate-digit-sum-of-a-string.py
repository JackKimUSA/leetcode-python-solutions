#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 19:38:57 2022

@author: Jack Kim
"""
"""
Problem:
You are given a string s consisting of digits and an integer k.

A round can be completed if the length of s is greater than k. In one round, do the following:

1. Divide s into consecutive groups of size k such that the first k characters are in the first group, 
the next k characters are in the second group, and so on. 
Note that the size of the last group can be smaller than k.

2. Replace each group of s with a string representing the sum of all its digits.
For example, "346" is replaced with "13" because 3 + 4 + 6 = 13.

3. Merge consecutive groups together to form a new string. 
If the length of the string is greater than k, repeat from step 1.

Return s after all rounds have been completed.
"""

class Solution:
    def groupsum(self, group: str) -> str:
        sum=0
        for i in group: sum += int(i)
        return str(sum)
    def digitSum(self, s: str, k: int) -> str:
        if len(s) <= k: return s
        
        while len(s) > k:
            result=[]
            while s:
                if len(s) > k:
                    result.append(self.groupsum(s[:k]))
                    s=s[k:]
                else:
                    result.append(self.groupsum(s))
                    break
            s="".join(result)
        return s
    

"""
Submissions:
Runtime: 38 ms, faster than 50.21% of Python3 online submissions for Calculate Digit Sum of a String.
Memory Usage: 14 MB, less than 14.64% of Python3 online submissions for Calculate Digit Sum of a String.
"""

S=Solution()
s="11111222223"
k=3
print(S.digitSum(s, k))