#User Input for Financial Details
monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your total monthly expenses: "))

#Calculate Monthly Savings
monthly_Savings = monthly_income - monthly_expenses

#Calculate Project Annual Savings:
Projected_Savings = monthly_Savings * 12 + (monthly_Savings * 12 * 0.05)

#Output
print(f"Your Monthly Savings are ${monthly_Savings}")
print(f"Projected savings after one year, with interest, is: ${Projected_Savings}")