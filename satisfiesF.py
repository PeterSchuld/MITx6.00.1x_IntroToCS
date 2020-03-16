# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 13:32:34 2019

@author: peter
"""

def satisfiesF(L):
    """
    Assumes L is a list of strings
    Assume function f is already defined for you and it maps a string to a Boolean
    Mutates L such that it contains all of the strings, s, originally in L such
            that f(s) returns True, and no other elements. Remaining elements in L
            should be in the same order.
    Returns the length of L after mutation
    """
    # Your function implementation here
    L_old=L[:]
    Liste=[]
    for l in L_old:
        if f(l)==True:
            Liste.append(l)
        elif f(l)==False:
            L.remove(l)
    L=Liste
    return(len(Liste))

def f(s):
    return 'a' in s

L = ['a', 'b', 'a']
print(satisfiesF(L))
print(L)        