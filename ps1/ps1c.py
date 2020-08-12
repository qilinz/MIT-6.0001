#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 22:10:59 2020

@author: karin
"""

portion_down_payment = 0.25
r = 0.04
semi_annual_rise = 0.07
total_cost = 1000000
months_need = 36

down_payment = portion_down_payment*total_cost

annual_salary = float(input("Enter the starting salary:"))

            
low = 0
high = 10000
num_guesses = 0

while True:
    portion_saved = int((high+low)/2)
    current_savings = 0
    monthly_salary = annual_salary/12
    for i in range(1,37):
        current_savings = monthly_salary*portion_saved/10000.0 + current_savings*(1+r/12)
        if i % 6 == 0:
            monthly_salary *= (1+semi_annual_rise)
    
    if abs(current_savings - down_payment)>100:
        if current_savings - down_payment >100:
            high = portion_saved
        else:
            low = portion_saved
            if low == high:
                 print('It is not possible to pay the down payment in three years.')
                 break
        num_guesses +=1
    else:
        print("Best savings rate:", portion_saved/10000)
        print("Steps in bisection search",num_guesses)
        break
        
    
    
            
            
