#1 Construct code that asks the user to provide their name, house / flat number and their street number or name.. Concatenate this information to display a message such as the following. (Attempt to write the message by using one single line of code, and ensure it is displayed on two separate lines, as shown.)
#From: Name
#Address: Full Address
#Message:
#Why was there a bug in the computer?
#Because it was looking for a "byte" to eat.

name = (input("Enter your name: "))
house_number = (input("Enter your house/flat number: "))
street_name = (input("Enter your street number or name: "))
message = ("Why was there a bug in the computer?\nBecause it was looking for a \"byte\" to eat.")

house_street = house_number + " " + street_name
print("From: " + name + "\nAddress: " + house_street + "\nMessage:\n" + message)

#2 Construct code that allows the user to enter their first and last names. Concatenate the two values, add a space in between and display the full name together with its length without the space.

name_first = (input("Enter your first name: "))
name_last = (input("Enter your last name: "))
full_name = name_first + " " + name_last
length_full_name = len(full_name) - 1  # Subtracting 1 to exclude the space
print("Length of Full Name (excluding space): " + str(length_full_name))

#3 Construct code that allows the user to enter a noun and a letter. Replace all occurrences of that letter with the @ symbol.
noun = (input("Enter a noun: "))
letter = (input("Enter a letter to replace: "))
modified_noun = noun.replace(letter, "@")
print("Modified Noun: " + modified_noun)    