# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 16:08:53 2019

@author: peter
"""

"""

Exercise 6:
    
Write a function to flatten a list. The list contains other lists, strings, 
or ints. For example, [[1,'a',['cat'],2],[[[3]],'dog'],4,5] is flattened 
into [1,'a','cat',2,3,'dog',4,5] (order matters).
"""

#code
def flatten(aList):
    ''' 
    aList: a list 
    Returns: a copy of aList, which is a flattened version of aList 
    '''
    
    if aList == []:
        return []
    else:
        for elem in aList:
            print((elem),(type(elem)==list)
            if type(elem) == list:
                aList.remove(elem)
                return flatten(elem) +flatten(aList)
            else:
                aList.remove(elem)
                return [elem] + flatten(aList)
            
print(flatten([[1,'a',['cat'],2],[[[3]],'dog'],4,5]))            