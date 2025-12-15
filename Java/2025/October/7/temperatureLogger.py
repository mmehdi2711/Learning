highest = -1
lowest = 999

for i in range (1, 8): #should be 8 so that it asks for 7 days
    temp = int(input("What is the temperature today?: "))
    if temp > highest:
        highest = temp
    elif temp < lowest:
        lowest = temp

print(f"The lowest recorded temperature is {lowest} degrees.")
print(f"The highest recorded temperature is {highest} degrees.")
