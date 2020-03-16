# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 18:57:37 2019

@author: peter
"""
def gcdRecur(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    #def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''

    # Your code here
    # Base case is when b = 0
    if b == 0:
        return a

    # Recursive case
    return gcdRecur(b, a % b)

print(gcdRecur(340, 238))
