print("Welcome to the tip calculator.")
bill = input("What was the total bill? $")
bill_new = float(bill)
tip = input("What percentage tip would you like to give? 10, 12, or 15? ")
people = input("How many people to split the bill?")
bill_new = bill_new + bill_new*int(tip)/100
payment = bill_new / int(people)
#payment = round(payment ,2)
print(f"Each person should pay: ${round(payment , 2)}")





