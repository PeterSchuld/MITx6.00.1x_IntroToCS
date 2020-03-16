# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 11:04:33 2019

@author: peter
"""

def getSublists(L,n):
    """ 
    L is a listz of integers
    n is an integer
    
    returns all sublists of L with with n elements
    """
    answer=[]
    for i in range(len(L)-(n-1)):
        answer.append(L[i:i+n])
            
    return(answer)    
    
    
print(getSublists([1, 1, 1, 1, 4],2))
    