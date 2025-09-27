grade = int(input("What is your grade? (number only): "))
average_score = int(input("What is your average score? (number only): "))

if grade >= 12:
    if average_score >= 90:
        print("You qualify for a full scholarship!")
    elif average_score >= 89>=75:
        print("You qualify for a partial scholarship.")
    else:
        print("You do not qualify for a scholarship.")
else:
    print("You do not qualify for a scholarship, due to being under Grade 12.")