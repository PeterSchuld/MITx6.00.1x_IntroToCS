# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 18:57:37 2019

@author: peter
"""
def gcdIter(a, b):
    if a<=b:
        divisor=a
    else:
        divisor=b
        
    while True:
        if a%divisor==0 and b%divisor==0:
            break
        else:
            divisor -=1
            
    print('GCD of ',a,'and',b,'is:',divisor)     
    
gcdIter(17, 12)    