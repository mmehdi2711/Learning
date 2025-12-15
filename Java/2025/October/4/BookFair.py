#
# During a school book fair, the following fixed prices apply:
#- Novel : 8.00
#- Comic : 5.00
#
#Task: Write a program to accomplish the following:
#The program first asks for the number of customers.
#For each customer:
#    -Input the book type.
#    -Input the amount of copies the customer wants.
#    -Add the total cost to the running revenue.
#    -Update the total count for each book type. 
#    -Determine which book type has a higher total order.
#At the end, the program should output the following with suitable messages:
#    1. The total number of books sold. 
#    2. The total revenue from sales.
#    3. The number of Novels and Comics sold.
#    4. The book type with the higher total order.
#
#

novel = 8.00
comic = 5.00

novel_sold = 0
comic_sold = 0
total_sold = 0
total_revenue = 0

customers = int(input("Enter number of customers: "))
for customer in range (1, customers + 1):
    while True:
        print(f"Customer {customer}:")
        book_type = input("Enter book type (Novel/Comic): ")
        amount_copies = int(input("Enter number of copies: "))
        if book_type == "Novel":
            novel_sold += amount_copies
            total_revenue = total_revenue + (novel * amount_copies)
            total_sold = total_sold + amount_copies
            break
        elif book_type == "Comic":
            comic_sold += amount_copies
            total_revenue = total_revenue + (comic * amount_copies)
        total_sold = total_sold + amount_copies
        break

print(f"Total number of books sold: {total_sold}.")
print(f"Total revenue from sales: $ {total_revenue}")
print(f"Number of Novels sold: {novel_sold}.")
print(f"Number of Comics sold: {comic_sold}.")
if novel_sold > comic_sold:
    print("The book type with the higher total order is Novel.")
else:
    print("The book type with the higher total order is Comic.")