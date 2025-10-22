# tip calculator
print("Welcome to the tip calculator!")
bill = int(input("what was the total bill?"))
tip = int(input("How much tip would you like to give? 10,12 or 15\n"))
person = int(input("How many person to split the bill?"))
money = ((bill/person)* tip/100 + bill/person)
print(f"Each person should pay {money}")