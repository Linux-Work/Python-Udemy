#  lists in python


states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts",
 "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island",
  "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama",
   "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota",
    "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota",
     "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]

print(states_of_america[20])

# if you want to count from the last then start indexing from -1 to ...
# you can't start from -0 beacouse there is no such thing exists in mathematics
print(states_of_america[-1])

# change the value stored in an index of the list 
states_of_america[0] = "Dell Aware"
print(states_of_america[0])

# print(states_of_america)

# adding elements in the list using append function
states_of_america.append("Mohitur Rahaman")

print(states_of_america)
