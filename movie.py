valid_day = ["saturday", "sunday","monday", "tuesday", "wednesday", "thursday", "friday"]

name= input("Enter your name: ")
age = int(input('Enter yor age: '))
day = input("Enter the day: ").lower()
student = input("Are you a student: ")

print ("-"*20)

if age <0:
    print ("invalid age")
elif day not in valid_day:
    print("invalid day")
else:
    if age <5:
        price = 0 
    elif age <=12:
        price = 6
    elif age <=59:
        price=10
    else:
        price =7

    if price == 0:
        print(f"{name} your ticket price is free")
    else :
        if day == "friday":
            price+=2
        if student == "yes":
            price *=0.8
        print(f"{name} your Ticket price is {price :.2f} SR")