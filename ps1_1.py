# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
annual_salary=int(input("your annual salary"))
portion_saved = 5000
total_cost = 1000000
semi_annual_raise = 0.07

portion_down_payment=total_cost*0.25
current_savings = 0
r=0.04
monthly_salary = annual_salary/12
upperbound=10000
lowerbound=0

months=0
while months!=36:
    current_savings += (current_savings*r/12 + float(monthly_salary*portion_saved/10000))
    months+=1
    if months%6 == 0:
        monthly_salary += monthly_salary*semi_annual_raise
    if months == 36:
        if abs(current_savings - portion_down_payment) < 100:
            print("end")
            break
        elif current_savings > portion_down_payment:
            months=0
            current_savings=0
            monthly_salary = annual_salary/12
            upperbound=portion_saved
            portion_saved=(portion_saved+lowerbound)//2
            continue
        elif current_savings < portion_down_payment:
            months=0
            current_savings=0
            monthly_salary = annual_salary/12
            lowerbound=portion_saved  
            portion_saved = (portion_saved+upperbound)//2
            continue
        else:
            print("error")
            break
    if abs(lowerbound-upperbound) == 1:
        print("impossible")
        break

print(portion_saved/10000)
