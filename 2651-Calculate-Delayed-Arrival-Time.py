#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 19:38:57 2022

@author: Jack Kim
"""
"""
Problem:
You are given a positive integer arrivalTime denoting the arrival time of a train in hours, 
and another positive integer delayedTime denoting the amount of delay in hours.

Return the time when the train will arrive at the station.
Note that the time in this problem is in 24-hours format.

Constraints:
1 <= arrivaltime < 24
1 <= delayedTime <= 24
"""


class Solution1:
    def findDelayedArrivalTime(self, arrivalTime: int, delayedTime: int) -> int:
        reachTime = arrivalTime + delayedTime
        if reachTime == 24:
            return 0
        if reachTime > 24:
            return reachTime - 24
        else:
            return reachTime

"""
Submissions:
Runtime 52ms    Beats 10.46%   Memory 16.2MB  Beats 35.83%
"""

class Solution:
    def findDelayedArrivalTime(self, arrivalTime: int, delayedTime: int) -> int:
        return (arrivalTime + delayedTime) % 24

"""
Submissions:
Runtime 44ms   Beats 29.58%   Memory 16.3MB  Beats 22.15%
"""

S=Solution()
print(S.findDelayedArrivalTime(15,5))
print(S.findDelayedArrivalTime(13,11))
print(S.findDelayedArrivalTime(1,24))