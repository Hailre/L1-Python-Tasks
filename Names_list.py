#Task 1
names = ("Evi", "Madeleine", "Dan", "Kelsey", "Cayden", "Hayley", "Darian")
print(sorted(names))




#Task 2 -  Get a user to enter a name and then check to see if the name is in the list
username = input("What is your name?").strip().title()

if username in names:
  print("Your name is already in the list")
else:
  print(f"Sorry {username} is not in the list")
