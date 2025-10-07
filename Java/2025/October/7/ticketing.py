b  child = 5   
teen = 8
adult = 12
total_price = 0
tickets = int(input("How many tickets do you want to buy?"))
for i in range (1, tickets + 1):
    age = int(input(f"How old is the holder of ticket {i}."))
    if age < 12:
        total_price = total_price + child
    elif age < 18:
        total_price = total_price + teen
    else:
        total_price = total_price + adult
if total_price > 50:
    total_price *= 0.9
    print("A 10% discount has been applied due to the price being over $50")

print(f"The total price is {total_price}. Enjoy the event!")
