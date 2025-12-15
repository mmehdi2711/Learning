
#Problem 1: School Library Late Fees 
#The Washington High School library has a late fee policy for overdue books. 
# Students pay $0.50 per day for the first 7 days a book is late. 
# If a book is 8-14 days late, the daily fee increases to $1.00 per day for those additional days. 
# If a book is more than 14 days late, the student must pay a flat fee of $25.00 regardless of how many days late it is. 
# However, if the student is a senior (grade 12), they get a 50% discount on any late fee. 
# Write a program that asks for the number of days late and the student's grade level, then calculates and displays the total late fee.

days_late = int(input("Enter the number of days the book is late: "))
grade_level = int(input("Enter the student's grade level (number only): "))
late_fee = 0.0
if days_late <= 7:
    late_fee = days_late * 0.50
elif days_late <= 14:
    late_fee = (7 * 0.50) + ((days_late - 7) * 1.00)
else:
    late_fee = 25.00
if grade_level == 12:
    late_fee *= 0.5
print("Total late fee: $" + format(late_fee, '.2f'))
