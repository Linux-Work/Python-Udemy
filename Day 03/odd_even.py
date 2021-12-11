#  testing a number is even or odd


number = int(input("Enter a number : "))
remainder = number % 2
if remainder == 1:
    print("This is an odd number.")
else:
    print("This is an even number.")