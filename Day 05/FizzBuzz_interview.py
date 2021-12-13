# fizz buzz interview question

#  if a number is divisible by 3 completely then type Fizz
#  if a number is divisible by 5 completely then type Buzz
#  if a number is divisible by 3 & 5 both then type FizzBuzz

total = 0
for number in range(1,101):
    if number % 3 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
