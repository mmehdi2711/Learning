# Fixed medicine prices
PARACETAMOL_PRICE = 2.00
ANTIBIOTIC_PRICE = 10.00
VITAMIN_PRICE = 5.00

# Counters
total_sales = 0.0
total_medicines = 0
paracetamol_count = 0
antibiotic_count = 0
vitamin_count = 0
# Step 1: Ask for number of patients

num_patients = int(input("Enter the number of patients today: "))

# Step 2: Process each patient
for i in range(num_patients):
    print("\nPatient", i+1)

    # Ask until a valid choice is given
    choice = input("Enter medicine (Paracetamol / Antibiotic / Vitamin): ")
    
    if choice == "Paracetamol":
        total_sales = total_sales + PARACETAMOL_PRICE
        paracetamol_count = paracetamol_count + 1

    if choice == "Antibiotic":
        total_sales = total_sales + ANTIBIOTIC_PRICE
        antibiotic_count = antibiotic_count + 1

    if choice == "Vitamin":
        total_sales = total_sales + VITAMIN_PRICE
        vitamin_count = vitamin_count + 1
        
    total_medicines = total_medicines + 1

# Step 3: Output results
print("\n--- Daily Report ---")
print("Total medicines sold:", total_medicines)
print("Total revenue: $", total_sales)
print("Paracetamol sold:", paracetamol_count)
print("Antibiotic sold:", antibiotic_count)
print("Vitamin sold:", vitamin_count)
