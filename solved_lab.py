age = int(input("Enter your age: "))
if age <= 0:
    print("Age cannot be zero or negative.")
    exit()

day = input("Enter The day: ")
if day.lower() not in ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]:
    print("Invalid day.")
    exit()

is_student = input("are you a student (y or n): ")
if is_student.lower() not in ["y", "n"]:
    print("Invalid input for student status.")
    exit()

if age < 5:
    price = "Free"
elif 12 >= age >= 5:
    price = 6
elif 59 >= age > 12:
    price = 10
else:
    price = 7

if price != "Free":
    if day.lower() == "friday" and price > 0:
        price += 2

if price != "Free":
    if is_student.lower() == "y" and price > 0:
        price -= (price * (20/100))

if price == "Free":
    print("Ticket price is: Free")
else:
    print(f"Ticket price is: ${price:.2f}")