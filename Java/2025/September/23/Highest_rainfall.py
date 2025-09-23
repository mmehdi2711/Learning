total_rainfall = 0
highest_rainfall = -1
lowest_rainfall = 99999

for day in range(1, 8):
    rain = float(input("Enter rainfall for day" + str(day) + "(in mm): "))
    total_rainfall = total_rainfall + rain