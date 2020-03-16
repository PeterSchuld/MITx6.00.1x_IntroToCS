# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 11:47:15 2019

@author: peter
"""
    
# balance - the outstanding balance on the credit card
# annualInterestRate - annual interest rate as a decimal
# monthlyPaymentRate - minimum monthly payment rate as a decimal
#Monthly interest rate= (Annual interest rate) / 12.0
#Minimum monthly payment = (Minimum monthly payment rate) x (Previous balance)
#Monthly unpaid balance = (Previous balance) - (Minimum monthly payment)
#Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance) 


balance=484
annualInterestRate=0.2
monthlyPaymentRate = 0.04

for x in range(1,13):
    balance = balance-monthlyPaymentRate*balance+(annualInterestRate/12)*(balance-monthlyPaymentRate*balance)
    balance=round(balance,2)
    print('Month',x,'Remaining balance: ',balance)
print(round(balance,2))    