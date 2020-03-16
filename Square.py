# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 10:16:23 2019

@author: peter
"""

def Square(x):
    return SquareHelper(abs(x), abs(x))

def SquareHelper(n, x):
    if n == 0:
        return 0
    return SquareHelper(n-1, x) + x

print(Square(-100))

