# typecasting is a process to change data types 
# like str to int

# use 'type' function to investigate the data type of a variable

# num_char = str(len(input("What is your name ?\n")))

num_char = len(input("What is your name ?\n"))
new_num_char = str(num_char)
print("Yorur name has " + new_num_char + " characters.")