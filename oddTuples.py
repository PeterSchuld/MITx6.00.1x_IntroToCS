# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 14:36:29 2019

@author: peter
"""

def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    # Your Code Here
    newTup=()
    for i in range(len(aTup)):
        if i%2==0:
            newTup=newTup+(aTup[i:i+1])
            
    return(newTup)

aTup=('I', 'am', 'a', 'test', 'tuple')

print(aTup)

print(oddTuples(aTup) )     