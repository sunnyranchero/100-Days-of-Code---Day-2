#Create a calculator helps us split the bill
#If the bill was $150.00, split between 5 people, with a 12% tip...

print("Hello, welcome to the bill splitter extrodinair.")
bill_amt = float(input("How much is the bill before the tip?\n"))
tip_percentage = int(input("How much would you like to tip? (10, 12, or 15 percent)?\n"))
people_count = int(input("How many people did you want to split this with?\n"))

tip_amt = bill_amt * int(tip_percentage) / 100
split_bill_total = round((bill_amt + tip_amt)/people_count, 2)
final_answer = "{:.2f}".format(split_bill_total)

print(f"Each person should pay: ${final_answer}")
