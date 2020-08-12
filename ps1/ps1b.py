#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 21:08:24 2020

@author: karin
"""


portion_down_payment = 0.25
current_savings = 0
r = 0.04
months_need = 0

annual_salary = float(input("Enter your annual salary:"))
portion_saved = float(input("Enter the percentage of your salary to save, as a demimal:"))
total_cost = float(input("Enter the cost of your dream home:"))
semi_annual_rise = float(input("Enter the semi­annual raise, as a decimal:"))
monthly_salary = annual_salary/12



while current_savings < total_cost*portion_down_payment:
    months_need +=1
    current_savings = monthly_salary*portion_saved + current_savings*(1+r/12)
    if months_need % 6 == 0:
        monthly_salary *= (1+semi_annual_rise)
    
print("Number of months:", months_need)