age = int(input("Enter your age: "))
day = input("Enter the day: ").lower()
choice = input("Are you a student? ").lower()
ticket_price = 0

if age < 0:
    print("Invalid age")
elif day not in ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]:
    print("Invalid day")
elif age < 5:
    print("Ticket Price: Free")
else:
    if age <= 12:
        ticket_price = 6
    elif age <= 59:
        ticket_price = 10
    else:
        ticket_price = 7

    if day == "friday":
        ticket_price += 2
    if choice == "yes":
        ticket_price *= 0.8

    print(f"Ticket Price: ${ticket_price:.2f}")
