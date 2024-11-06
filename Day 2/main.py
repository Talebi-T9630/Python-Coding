#Tip Calculator
total = float(input("What was the total bill?"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15?"))
people =int(input("How many people are splitting the bill?"))

final_cost = (total+((tip/100)*total))/people

print(f"Each person pays: {round(final_cost,2)}")