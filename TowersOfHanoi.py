# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 14:24:32 2019

@author: peter
"""

def printMove(fr, to):
    print('movefrom ' + str(fr) + ' to '+ str(to))
    
def Towers(n, fr, to, spare):
    if n== 1:
        printMove(fr, to)
    else:
        Towers(n-1, fr, spare, to)
        Towers(1, fr, to, spare)
        Towers(n-1, spare, to, fr)