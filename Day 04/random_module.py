#  python randomization with random module


import random
import my_module


# random_integer = random.randint(1,10)
# print(random_integer)

# # print(my_module.pi)

# random_float = random.random() # random function only gives value from 0.00000000 to 0.9999999...

# print(random_float)

# # but if you want to increase the range, just multiply the limit
# random_float1 = random.random()  * 5
# # this will print random floats from 0.0000... to 4.9999...
# print(random_float1)


love_score = random.randint(1, 100)
print(f"Your love score is {love_score}")