# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 13:07:26 2019

@author: peter
"""

def fancy_divide(list_of_numbers, index):
   denom = list_of_numbers[index]
   return [simple_divide(item, denom) for item in list_of_numbers]


def simple_divide(item, denom):
    try:
        a=item/ denom
        
    except ZeroDivisionError:    
        a=0
    finally:
        return(a)


print(fancy_divide([0, 2, 4], 0))