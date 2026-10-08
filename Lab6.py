

age = int(input("Enter your age: "))
day = input("Enter the day: ").strip().capitalize()
student = input("Are you a student? ").strip().lower()
valid_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
              

if age < 0:
    print("Invalid age")
elif day not in valid_days:
    print("Invalid day")
else:
    # prices by agee
    if age < 5:
        price = 0
    elif age <= 12:
        price = 6
    elif age <= 59:
        price = 10
    else:
        price = 7

    # the free tik 
    if price == 0:
        print("Ticket price: Free")
    else:
        
        if day == "Friday":
            price = price + 2
        if student == "yes":
            price = price * 0.8
        print(f"Ticket price: ${price:.2f}")
        