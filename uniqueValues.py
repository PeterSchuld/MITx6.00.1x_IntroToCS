# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 11:29:00 2019

@author: peter
"""

def uniqueValues(aDict):
    '''
    aDict: a dictionary
    returns a list of keys in aDict that map to integer values that are unique 
    (i.e. values appear exactly once in aDict). 
    The list of keys you return should be sorted in increasing order. 
    (If aDict does not contain any unique values, you should return an empty list.)
    '''
    # Your code here
   
    L=[]
    Schluessel=[]
    L_all=[]
    
    for x in aDict.keys():
        L_all.append(aDict[x])
       
    
    for k in aDict.keys():
        if (aDict[k]) not in L:
            L.append(aDict[k])
            L_all.remove(aDict[k])
            if (aDict[k]) not in L_all:
                Schluessel.append(k)
        
    Schluessel.sort()        
    return(Schluessel)        





grades = {'Ana':'B', 'John':'A+', 'Denise':'A', 'Katy':'A'}
print(uniqueValues(grades))

print(uniqueValues({1: 1, 3: 2, 6: 0, 7: 0, 8: 4, 10: 0}))

#Your output:

#    [1, 3, 6, 8]

#Correct output:

#    [1, 3, 8]

