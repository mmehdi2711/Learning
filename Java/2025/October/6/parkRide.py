height = int(input("Enter your exact height in centimetres (cm): "))
if height < 100:
    print("You are too short to ride.")
elif height < 140:
    print("You can ride with an adult. Enjoy!")
else:
    print("You can ride alone. Enjoy!")
