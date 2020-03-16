# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 12:25:20 2019

@author: peter
"""
print("Please think of a number between 0 and 100!")
print("Is your secret number 50?")
x=input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")


epsilon = 0.01
numGuesses= 0
low = 0.0
high = x
ans= (high + low)/2.0
while abs(ans**2-x) >= epsilon:
    print('low= '+ str(low) + ' high = '+ str(high) + ' ans= ' + str(ans))
    numGuesses+= 1
    if ans**2< x:
        low = ans
    else:
        high = ans
    ans= (high + low)/2.0
print('numGuesses= ' + str(numGuesses))
print(str(ans) + ' is close to square root of ' + str(x))
