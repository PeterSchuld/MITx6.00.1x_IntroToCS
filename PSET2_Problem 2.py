# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 15:39:35 2019

@author: peter
"""

# balance - the outstanding balance on the credit card
# annualInterestRate - annual interest rate as a decimal

# Assume that the interest is compounded monthly according to the balance at the end of the month (after the payment for that month is made). The monthly payment must be a multiple of $10 and is the same for all months. Notice that it is possible for the balance to become negative using this payment scheme, which is okay. A summary of the required math is found below:

# Monthly interest rate = (Annual interest rate) / 12.0
# Monthly unpaid balance = (Previous balance) - (Minimum fixed monthly payment)
# Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)

balance = 3329; annualInterestRate = 0.2
monthlyPaymentRate = 0
init_balance = balance
monthlyInterestRate = annualInterestRate/12

while balance > 0:
    for i in range(12):
        balance = balance - monthlyPaymentRate + ((balance - monthlyPaymentRate) * monthlyInterestRate)
    if balance > 0:
        monthlyPaymentRate += 10
        balance = init_balance
    #elif balance <= 0:
    #    break
print('Lowest Payment:', monthlyPaymentRate)
