# Program to calculate total membership fees collected

TOTAL_MEMBERS = 10
FULL_FEE = 20
DISCOUNT_RATE = 0.20
         
total_fee = 0

print("Enter status for each member (1: new, 2: existing):")
for i in range(1, TOTAL_MEMBERS + 1):
    while True:
        try:
            status = int(input(f"Member {i} status: "))
            if status == 1:
                fee = FULL_FEE * (1 - DISCOUNT_RATE)
                total_fee += fee
                break
            elif status == 2:   
                fee = FULL_FEE
                total_fee += fee
                break
            else:
                print("Invalid input. Enter 1 for new or 2 for existing member.")
        except ValueError:
            print("Invalid input. Please enter a number (1 or 2).")
