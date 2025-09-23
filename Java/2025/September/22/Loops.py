n = int(input("ENter a positive interger: "))
total = 0
for count in range(1, n+1):
    if count % 2 ==0:
        total = total + count
print("The total is", total)
