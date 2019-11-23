#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 21:54:26 2019

@author: Jack Kim
"""

"""
Problem:
Given a valid (IPv4) IP address, return a defanged version of that IP address.
A defanged IP address replaces every period "." with "[.]".
"""

class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace('.', '[.]')
    
address="1.1.1.1"
S=Solution()
print(S.defangIPaddr(address))

"""
Submissions:
Runtime: 16 ms, faster than 99.90% of Python3 online submissions for Defanging an IP Address.
Memory Usage: 12.6 MB, less than 100.00% of Python3 online submissions for Defanging an IP Address.
"""