total_bill = float(input("What was the total bill? $"))
percentage = float(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = float(input("How many people to split the bill? "))
total_with_tip = (total_bill * (percentage * .01)) + total_bill
total_per_person = round(total_with_tip / people, 2)
total_per_person = "{:.2f}".format(total_per_person) # fixes the issue if total is something like 1.10
print(f"Each person should pay: ${total_per_person}")