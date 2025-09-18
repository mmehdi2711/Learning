# Area of a Rectangle

length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

area = length * width

print("The area of the rectangle is:", area)

# Area of a Circle

import math

radius = float(input("Enter the radius of the circle: "))

area = math.pi * radius ** 2

print("The area of the circle is:", area)


# Temperature Conversion

celsius = float(input("Enter temperature in Celsius: "))

fahrenheit = (celsius * 9/5) + 32

print("Temperature in Fahrenheit is:", fahrenheit)

# Simple Interest

principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest (in %): "))
time = float(input("Enter the time (in years): "))

simple_interest = (principal * rate * time) / 100

print("The Simple Interest is:", simple_interest)
