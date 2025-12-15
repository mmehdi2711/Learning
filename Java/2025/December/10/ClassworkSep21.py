# Counter-controlled loop questions
#1. Write a for loop in Python to show the multiplication table of a number.
#The program should ask the user to enter a number.
#Then use a for loop to print the multiplication table of that number up to 10.

number = int(input("Enter a number to display its multiplication table: "))
print(f"Multiplication table of {number}:")
for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")


#2. An electricity meter records units consumed each month. Write a program using a for loop
#to print units from 100 to 500 in steps of 100, like:

print("Electricity units from 100 to 500 in steps of 100:")
for units in range(100, 501, 100):
    print(units)

#3. Write a Python program that asks the user to enter the rainfall (in mm) for 7 days.
#After all inputs are entered, the program should calculate and display:
#The total rainfall for the week.
#The average rainfall.
#The highest rainfall in a single day.
#The lowest rainfall in a single day.

total_rainfall = 0
highest_rainfall = float(-1)
lowest_rainfall = float(999999999999999)
for day in range(1, 8):
    rainfall = float(input(f"Enter the rainfall (in mm) for day {day}: "))
    total_rainfall += rainfall
    if rainfall > highest_rainfall:
        highest_rainfall = rainfall
    if rainfall < lowest_rainfall:
        lowest_rainfall = rainfall 
average_rainfall = total_rainfall / 7
print(f"Total rainfall for the week: {total_rainfall} mm")
print(f"Average rainfall: {average_rainfall:.2f} mm")
print(f"Highest rainfall in a single day: {highest_rainfall} mm")
print(f"Lowest rainfall in a single day: {lowest_rainfall} mm")

