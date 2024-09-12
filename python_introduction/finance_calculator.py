#User Input for Financial Details
monthly_income = float(input("Enter your monthly income "))
total_expenses = float(input("Enter your total monthly expenses "))

#Calculate Monthly Savings
Monthly_Savings = monthly_income - total_expenses

#Calculate Project Annual Savings:
Projected_Savings = Monthly_Savings * 12 + (Monthly_Savings * 12 * 0.05)

#Output
print(f"Your Monthly Savings are ${Monthly_Savings}")
print(f"Projected savings after one year, with interest, is: ${Projected_Savings}")