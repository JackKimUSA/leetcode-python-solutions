#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 22:25:27 2020

@author: Jack Kim
"""

"""
Problem:
Say you have an array for which the ith element is the price of a given stock on day i.
If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), 
design an algorithm to find the maximum profit.
Note that you cannot sell a stock before you buy one.
"""

# Time Limit Exceeded
class Solution_1:
    def maxProfit(self, prices: int) -> int:
        max_price = 0
        
        for i, price in enumerate(prices):
            for j in range(i,len(prices)):
                max_price = max(prices[j] - price, max_price)
        return max_price

import sys
class Solution:
    def maxProfit(self, prices: int) -> int:
        profit = 0
        min_price = sys.maxsize
        
        for price in prices:
            min_price = min(min_price, price)
            profit = max(profit, price - min_price)
            
        return profit

"""
Submissions:
Runtime: 68 ms, faster than 20.09% of Python3 online submissions for Best Time to Buy and Sell Stock.
Memory Usage: 15 MB, less than 15.06% of Python3 online submissions for Best Time to Buy and Sell Stock.
"""
            
prices=[7,1,5,3,6,4]
S=Solution()
print(S.maxProfit(prices))