
age = int(input("Enter your age: "))
day = input("Enter the day: ")
is_student = input("Are you a student? ").strip().lower()

mjj=37

if age < 0:
    print("Invalid age")
elif day not in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]:
    print("Invalid day")
else:
    
    if age < 5:
        price = 0
    elif 5 <= age <= 12:
        price = 6
    elif 13 <= age <= 59:
        price = 10
    else:  
        price = 7

   
    if day == "Friday":
        price += 2

    
    if is_student == "yes" and price > 0:
        price = price * 0.8  

    
    if price == 0:
        print("Ticket price: Free")
    else:
        print(f"Ticket price: ${price:.2f}")