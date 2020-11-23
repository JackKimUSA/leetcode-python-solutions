#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 00:36:12 2020

@author: Jack Kim
"""

"""
Problem:
You have an array of logs.  Each log is a space delimited string of words.
For each log, the first word in each log is an alphanumeric identifier.  Then, either:
    - Each word after the identifier will consist only of lowercase letters, or;
    - Each word after the identifier will consist only of digits.
We will call these two varieties of logs letter-logs and digit-logs.  
It is guaranteed that each log has at least one word after its identifier.
Reorder the logs so that all of the letter-logs come before any digit-log.  
The letter-logs are ordered lexicographically ignoring identifier, with the identifier used in case of ties.  
The digit-logs should be put in their original order.

Return the final order of the logs.
"""
class Solution:
    def reorderLogFiles(self, logs: str) -> str:
        digits,letters=[],[]
        for log in logs:
            if log.split()[1].isdigit():
                digits.append(log)
            else:
                letters.append(log)
        
        letters.sort(key=lambda x:(x.split()[1:], x.split()[0]))
        return letters + digits
            
            

logs=["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
S=Solution()
print(S.reorderLogFiles(logs))
"""
Submissions:
Runtime: 40 ms, faster than 26.73% of Python3 online submissions for Reorder Data in Log Files.
Memory Usage: 14.4 MB, less than 13.57% of Python3 online submissions for Reorder Data in Log Files.
"""
