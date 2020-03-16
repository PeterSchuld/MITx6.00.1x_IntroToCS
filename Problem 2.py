# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 15:39:35 2019

@author: peter
"""


balance                  = 4773; 
annualInterestRate       = 0.2
monthlyInterestRate      = annualInterestRate/12
monthlyPaymentRate_lower = balance/12
monthlyPaymentRate_upper = (balance * (1 + monthlyInterestRate)**12) / 12.0
init_balance             = balance


# Monthly interest rate = (Annual interest rate) / 12.0
# Monthly payment lower bound = Balance / 12
# Monthly payment upper bound = (Balance x (1 + Monthly interest rate)12) / 12.0 


while balance > 0:
    for i in range(12):
        balance = balance - (monthlyPaymentRate_upper+monthlyPaymentRate_lower)/2 + ((balance - (monthlyPaymentRate_upper+monthlyPaymentRate_lower)/2) * monthlyInterestRate)
    if balance > 0:
        monthlyPaymentRate += 10
        balance = init_balance
    #elif balance <= 0:
    #    break
print('Lowest Payment:', monthlyPaymentRate)
