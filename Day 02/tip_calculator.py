print("Welcome to the tip calculator!")
bill = float(input("What was the tootal bill? $"))
tip = float(input("How much tip would you like to give? 10, 12, or 15? "))
total_bill = bill + (bill * (tip/100))
split = float(input('How many people to split the bill? '))
bill_per_head = total_bill/split
bill_per_head1 = str(round(bill_per_head, 2))
print("Each person should pay: " + bill_per_head1)