age = int (input("Enter your age:"))
day  =input("Enter the day:")
student = input("Are you a student?")

if age < 0 :
    print("Invalid age")
elif (day != "Monday" and
      day != "Tuesday" and
      day != "Wednesday" and
      day != "Thursday" and
      day != "Friday" and
      day != "Saturday" and
      day != "Sunday"):
    print("Invalid day")
else:
    if age < 5:
        prica = 0
    elif age <= 12:
        prica = 6
    elif age <= 59:
        prica = 10
    else:
        prica = 7

    if prica == 0:
        print("Ticket price: Free")
    else:
        if day == "Friday":
            prica = prica + 2

        if student == "yes":
            prica = prica * 0.8

        print(f"Ticket price: ${prica:.2f}")
