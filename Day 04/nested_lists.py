# Nessted list is a list which containing list inside it.


fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [fruits, vegetables]

print(dirty_dozen)
 
print(dirty_dozen[1][2])
# here 1 is trying to say this is the second list vegetables, because fruits is the 1st list & assigned 0
# 2 is trying to say no. 2 index
# dirty_dozen[1][2] means index 2 element of the vegetables list 

