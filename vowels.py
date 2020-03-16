# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 10:23:07 2019

@author: peter
"""

s="azcbobobegghakl"
result = []
final = []

for letters in s:
    result = result + [letters]
    if result == sorted(result) and len(result) >= len(final):
        final = result
    elif result != sorted(result):
        result = [result[len(result)-1]]
print('Longest substring in alphabetical order is: '+(''.join(final)))