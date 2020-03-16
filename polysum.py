# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 13:29:42 2019

@author: peter
"""

def polysum (n,s):
        """
        input
        n is an int or float
        s is an int of float
        return
        sum, rounded to 4 decimal places
        """
        import math
        sum =  (0.25*n*s**2)/math.tan(math.pi/n)
        area_of_polygon = (0.25 * n * s ** 2) / math.tan(math.pi / n)
        perimeter_of_polygon_squared = (n * s) ** 2

        return round(area_of_polygon + perimeter_of_polygon_squared, 4)
        
        
print (polysum(81,86) )       


#Test: polysum(81, 86)


#Correct output:

#    52384728.7584

