print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

final = bill/people * (1+(tip/100))
final = round(final,2)
print(f"You must pay: ${final}")
