# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 16:40:49 2019

@author: peter
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 15:05:26 2017
@author: Mayur
"""
"""
Exercise 5:
Write a Python function that returns a list of keys in aDict with the value 
target. The list of keys you return should be sorted in increasing order. 
The keys and values in aDict are both integers. (If aDict does not contain 
the value target, you should return an empty list.)
This function takes in a dictionary and an integer and returns a list.
"""

#code
def keysWithValue(aDict, target):
    '''
    aDict: a dictionary
    target: an integer
    '''
    keys = []
    for key in aDict:
        if aDict[key] == target:
            keys.append(key)
    return sorted(keys)

a=dict([(3,"three"),(1,"one"),(2,"two")])
print(keysWithValue(a, 1))
print(type(a))