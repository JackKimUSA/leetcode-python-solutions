#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 22:56:53 2019

@author: jgkim
"""

"""
Problem:
Balanced strings are those who have equal quantity of 'L' and 'R' characters.
Given a balanced string s split it in the maximum amount of balanced strings.
Return the maximum amount of splitted balanced strings.
"""

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        max_num, l_num, r_num = 0, 0, 0
        for c in s:
            if c == 'L':
                l_num += 1
            else:
                r_num += 1
            if l_num == r_num:
                max_num += 1
        return max_num

#s="RLRRLLRLRL"
#s="RLLLLRRRLR"
#s="LLLLRRRR"
#s="RLRRRLLRLL"
s="RRLRRLRLLLRL"

Sol=Solution()
print(Sol.balancedStringSplit(s))

"""
Submissions:
Runtime: 20 ms, faster than 99.48% of Python3 online submissions for Split a String in Balanced Strings.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Split a String in Balanced Strings.
"""