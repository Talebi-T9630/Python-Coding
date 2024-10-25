#Tip Calculator
total = input("What was the total bill?")
tip = input("What percentage tip would you like to give? 10, 12, or 15?")
people = input("How many people are splitting the bill?")

final_cost = (float(total)+((float(tip)/100)*float(total)))/float(people)

print(f"Each person pays: {round(final_cost,2)}")