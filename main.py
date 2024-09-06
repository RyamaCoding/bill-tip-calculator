welcome = "Welcome to the tip calculator."
print(welcome)
bill = input("What was the total bill amount? $")
tip = input("What percentage tip would you like to give? 10, 12, or 15? ")
split = input("How many people are splitting the bill? ")

final = float(bill) * (1 + (int(tip) / 100))
individual = final / int(split)

print(f"The final amount per person is: ${individual:.2f}")