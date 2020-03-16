# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 14:48:18 2019

@author: peter
"""
#Test Case 1:
balance = 4773
annualInterestRate = 0.2
#Result Your Code Should Generate:
#-------------------
#Lowest Payment: 310


# Monthly interest rate = (Annual interest rate) / 12.0
# Monthly unpaid balance = (Previous balance) - (Minimum fixed monthly payment)
# Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance) 

# Paste your code into this box

fixedMonthlyPayment=10.0
while balance>0:
    for i in range(12):
        balance = balance - (fixedMonthlyPayment) + ((balance - (fixedMonthlyPayment)) * (annualInterestRate/12))
        print("Remaining balance:", round(balance, 2))
    fixedMonthlyPayment += 10
    
print('Lowest Payment:',fixedMonthlyPayment)    