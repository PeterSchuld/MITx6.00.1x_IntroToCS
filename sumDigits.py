# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 12:53:27 2019

@author: peter
"""

def sumDigits(N):
    '''
    N: a non-negative integer
    '''
    if N == 0:
        return 0
    elif N % 10 != 0:
        return N % 10 + sumDigits(N // 10)
    else:
        return 0 + sumDigits(N // 10) 
    
print(sumDigits(1111666660000))    