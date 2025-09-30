n = int(input("Enter a positive integer: "))
total = 0
for count in range(1, n+1):
    if count % 2 == 0:
        total = total + count
print(f"The total of all even numbers until {count} is", total)
