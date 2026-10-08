age = input("Please enter your age: "  )
age = int(age)
day = input("Please enter the day of the week: ")
day = str(day)
student = input("Are you a student? (yes/no): ")
student = str(student)

if age < 0:
    print("Invalid age.")
elif day not in ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]:
    print("Invalid day of the week.")
elif age < 5 :
    print("ticket price is free")
else:
    if age <=12:
        price = 6 
    elif age <= 59:
        price = 10
    else:
        price = 7
    if day == "friday":
        price = price +2 
    if student == "yes":
        price = price *0.8
    print(f"The ticket price is: ${price:.2f}")