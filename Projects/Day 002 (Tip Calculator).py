# Welcome to the Tip Calculator!
#If the bill was Rs 150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

# code 👇

print("Welcome to the Tip Calculator!")
bill = float(input("What was the total bill? "))
tip = int(input("How much tip would you like to give? "))
people = int(input("How many people to split the bill? "))

tip_percent = tip/100
total_tip = bill * tip_percent
total_bill = bill + total_tip
bill_person = total_bill/people
final_amount = round(bill_person, 2)

print(f"Each person should pay: Rs {final_amount}")