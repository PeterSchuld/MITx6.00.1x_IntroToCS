# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 13:53:22 2019

@author: peter
"""
# s = 'kwayqyzfidhkfxrq'
# Longest substring in alphabetical order is: qyz

s = 'qnojscygzllrfmpfmrjgini'
# Longest substring in alphabetical order is: llr
result = []
final = []

for letters in s:
    result = result + [letters]
    if result == sorted(result) and len(result) > len(final):
        final = result
    elif result != sorted(result):
        result = [result[len(result)-1]]
    print(letters,result)    
print('Longest substring in alphabetical order is: '+(''.join(final)))



#s = 'okletzlpfnffztitksdkj'
# Longest substring in alphabetical order is: etz

#s = 'ljqpecayr'
# Longest substring in alphabetical order is: jq
