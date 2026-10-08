age : int = int(input("Enter your age: "))

if age < 0 or age > 120:
    print("Invalid age")
    exit()  

day : str = input("Enter the day of the week : ").strip().lower()

if day != "saturday" and day != "sunday" and day != "monday" and day != "tuesday" and day != "wednesday" and day != "thursday"and day != "friday" :
    print("Invalid day  ")
    exit()
elif day == "friday" :
    print("You must pay $2.00 extra for the weekend .")


status : str = input("Are you a student? : ").strip().lower()

if status == "yes" and age >= 7 and age <= 30:
    print("u will get a student discount of 20%" )


price: float = 0.0

if age >= 0 and age <= 4:
    price = 0.0
elif age >= 5 and age <= 12:
    price = 6.0
elif age >= 13 and age <= 59:
    price = 10.0
else: 
    price = 7.0

if day == "friday" and price > 0:
    price += 2.0

if status == "yes" and price > 0:
    price *= 0.80

if price == 0:
    print(" ticket price: Free")
else:
    print(f"ticket price: ${price:.2f}")




