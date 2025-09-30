my_list = []
# x = 0 
student_count = int(input("How many students are in your class?:"))
for x in range(1, student_count+1):
    student_grade = int(input(f"Enter student {x}'s grade: "))
    print(f"Student {x}'s grade is {student_grade}")
    my_list.append(student_grade)

print(f"The value of x is {student_count}.")   

pass_mark = 50
total_marks = sum(my_list)
print(f"The total marks of the class is {total_marks}")
average_marks = sum(my_list) / student_count
print(f"The average marks of the class is {average_marks}")
highest_marks = max(my_list)
print(f"The highest marks of the class is {highest_marks}")
lowest_marks = min(my_list)
print(f"The lowest marks of the class is {lowest_marks}")


passing_students = []
failing_students = []

for grade in my_list:
    if grade >= pass_mark:
        passing_students.append(grade)
    else:
        failing_students.append(grade)


print(f"The number of passing students is {len(passing_students)}")
print(f"The number of failing students is {len(failing_students)}") 
