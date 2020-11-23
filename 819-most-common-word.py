#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 02:55:50 2020

@author: Jack Kim
"""

"""
Problem:
Given a paragraph and a list of banned words, return the most frequent word that is not in the list of banned words. 
It is guaranteed there is at least one word that isn't banned, and that the answer is unique.
Words in the list of banned words are given in lowercase, and free of punctuation.  
Words in the paragraph are not case sensitive.  The answer is in lowercase.
"""
import re

class Solution_1:
    def mostCommonWord(self, paragraph: str, banned: str) -> str:
        paragraph=re.sub('[^a-zA-Z0-9]', ' ', paragraph).lower()
        hash_p={}
        hash_v={}
        for word in paragraph.split():
            if word in hash_p.keys():
                hash_p[word]=hash_p[word] + 1
            elif word not in hash_p.keys():
                hash_p[word]=0
        
        print(hash_p)
        
        for del_ban in banned:
            if del_ban in hash_p.keys():
                del(hash_p[del_ban])
        
        for key, value in hash_p.items():
            hash_v[value]=key
        
        return hash_v[max(hash_p.values())]

"""
Submissons:
Runtime: 40 ms, faster than 22.26% of Python3 online submissions for Most Common Word.
Memory Usage: 14.5 MB, less than 21.81% of Python3 online submissions for Most Common Word.
"""

import collections                
    
class Solution:
    def mostCommonWord(self, paragraph: str, banned: str) -> str:
        words = [ 
            word for word in re.sub(r'[^\w]', ' ', paragraph).lower().split() 
            if word not in banned 
            ]
        counts = collections.Counter(words)
        
        return counts.most_common(1)[0][0]
    
"""
Submisstions:
Runtime: 32 ms, faster than 80.84% of Python3 online submissions for Most Common Word.
Memory Usage: 14.5 MB, less than 21.81% of Python3 online submissions for Most Common Word.
"""
    
#paragraph="Bob hit a ball, the hit BALL flew far after it was hit."
#paragraph="Bob. Hit, ball"
#paragraph="a."
paragraph="Bob!"
banned=["hit"]
#banned=["bob", "hit"]
#banned=[]

S=Solution()
print(S.mostCommonWord(paragraph, banned))
