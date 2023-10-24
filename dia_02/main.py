print("Welcome to the tip calculator.")
value = float(input("What was the total bill? "))
#print(f"RS$: {value}")
porcentage = int(input("What percentage tip would you like to give? 10, 12 or 15? "))
calculation = (porcentage / 100) * value + value
total_people = int(input("How many people to split the bill? "))
result = calculation / total_people
print(f"Each person should pay: {result:.2f}")