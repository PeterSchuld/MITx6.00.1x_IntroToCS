# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 13:32:31 2019

@author: peter
"""
def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''

    # Your code here
    result = 1
    while exp > 0:
        result *=base
        exp -= 1
    return result

base=10
exp=3        
answer=iterPower(base,exp)
print('Base :',base)
print('exp :', exp)


print('Answer :', answer)        