# rock paper scissors game in python


import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
comp_choice = random.randint(0,2)
if choice == 0:
    print("You choose : \n")
    print(rock)
    if comp_choice == 0:
        print("Computer chosen : \n")
        print(rock)
        print("Draw Match!")
    elif comp_choice == 1:
        print("Computer chosen : \n")
        print(paper)
        print("The computer has chosen paper, You lose!")
    else:
        print("Computer chosen : \n")
        print(scissors)
        print("The computer has chosen scissors, You win!")
elif choice == 1:
    print("You choose : \n")
    print(paper)
    if comp_choice == 0:
        print("Computer chosen : \n")
        print(rock)
        print("The computer has chosen rock, You win!")
    elif comp_choice == 1:
        print("Computer chosen : \n")
        print(paper)
        print("Draw Match!")
    else:
        print("Computer chosen : \n")
        print(scissors)
        print("The computer has chosen scissors, You lose!")
elif choice == 2:
    print("You choose : \n")
    print(scissors)
    if comp_choice == 0:
        print("Computer chosen : \n")
        print(rock)
        print("The computer has chosen rock, You lose!")
    elif comp_choice == 1:
        print("Computer chosen : \n")
        print(paper)
        print("The computer has chosen paper, You win!")
    else:
        print("Computer chosen : \n")
        print(scissors)
        print("Draw Match!")
else:
    print("You have given an invalid input.")