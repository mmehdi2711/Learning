total = 0
students = 1
marks = 0
while students <=10:
    marks = int(input(f"What is student {students}'s mark? "))
    total = total + marks
    students = students + 1

print (f"The total marks of the class is {total}")
average = total / 10
print (f"The average marks of the class is {average}")