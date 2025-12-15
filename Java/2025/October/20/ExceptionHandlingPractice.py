def calculate_fee():
    RATE_PER_HOUR = 5.0  

    while True:
        try:
            hours_input = input("Enter number of hours used: ").strip()
            
            hours = float(hours_input)

            if hours <= 0:
                print("Hours must be greater than zero. Please try again.\n")
                continue

            fee = RATE_PER_HOUR * hours
            print(f"Total fee: ${fee:.2f}")
            break 

        except ValueError:
            print("Invalid input. Please enter a number (e.g., 3 or 2.5).\n")
        except ZeroDivisionError:
            print("Cannot divide by zero hours. Please enter a valid number.\n")

calculate_fee()
