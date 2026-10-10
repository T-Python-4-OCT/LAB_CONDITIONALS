age = int(input("Enter your age: "))
day = input("Enter the day: ")
is_student = input("Are you a student? (yes or no): ")

if age < 0:
    print("Invalid age")
elif day not in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]:
    print("Invalid day")
else:
    if age < 5:
        ticket_price = 0
        price_str = "Free"
    elif 5 <= age <= 12:
        ticket_price = 6
        price_str = "$6.00"
    elif 13 <= age <= 59:
        ticket_price = 10
        price_str = "$10.00"
    else:
        ticket_price = 7
        price_str = "$7.00"

    if day.lower() == "friday" and ticket_price > 0:
        ticket_price += 2
        price_str = f"${ticket_price}.00"

    if is_student.lower() == "yes" and ticket_price > 0:
        ticket_price = ticket_price - (ticket_price * 0.20)
        price_str = f"${ticket_price:.2f}"

    print(f"Ticket price: {price_str}")