# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 13:32:31 2019

@author: peter
"""

def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    # Your code here
    
    if exp==0:
        return(1)
    elif exp==1:    
        return(base)
    else:
        return(base * recurPower(base,exp-1))

base=10
exp=3        
answer=recurPower(base,exp)
print('Base :',base)
print('exp :', exp)


print('Answer :', answer)        