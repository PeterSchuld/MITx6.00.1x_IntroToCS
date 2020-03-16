# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 15:34:18 2019

@author: peter
"""

def count7(N):
    if N==0:
        return(0)
    elif N&10==7:
        return (1+count7(N//10))
    else:
        return (0+count7(N//10))
    
print(count7(107))   


def count7(N):
    '''
    N: a non-negative integer
    returns: no. of occurrences of digit 7 in the number N
    '''
    if N == 0:
        return 0
    elif N % 10 == 7:
        return 1 + count7(N // 10)
    else:
        return 0 + count7(N // 10) 