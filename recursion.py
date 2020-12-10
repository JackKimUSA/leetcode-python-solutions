#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 01:57:29 2020

@author: Jack Kim
"""

def countdown(x):
    if x == 0:
        print("done")
        return
    else:
        print(x)
        countdown(x-1)
        print("foo")

countdown(4)

def power(num, pwr):
    if pwr == 0:
        return 1
    else:
        return num * power(num, pwr-1)

print(power(2,4))
print(power(2,0))

def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num -1)

print(factorial(4))
print(factorial(0))

