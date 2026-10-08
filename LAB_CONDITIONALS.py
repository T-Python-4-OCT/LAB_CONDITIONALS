age:str = int(input ("Enter your age: "))
day:str = input ("Enter the day: ")
student:str = input ("Are you a student?: ")
valid_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

price = 0

if age < 0  or age >180:
    print ("Invalid age")
elif day not in valid_days:
    print("invalid day")
else:
    if age < 5:
        print ("Ticket price: free")
    else:
        if age <= 12:
            price = 6.00
        elif age <= 59:
            price = 10.00
        else:
            price = 7.00
        if day == "Friday":
            price += 2
        if student == "yes":
            price *=0.80
        print("Ticket price: $" + str(round(price, 2)))
        print ("Thank you for visiting.")