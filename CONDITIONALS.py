age:str=int(input("enter yuor age"))
day:str=(input("Choose a day of the week"))
student:str=(input(" are a student (yes or no)"))


Ticketprice=0

if age < 5:
    print("free")

elif age >=5 and age<12:
    Ticketprice=6.00
elif age >=12 and age<59:
    Ticketprice=10.00
elif age>60:
    Ticketprice=7.00
else:
    print("Invalid age")


if day == "Friday":
    print("Enter the day:",day)
elif day == "Monday" or day=="Sunday":
     print("Enter the day:",day)
elif day == "Tuesday" and day=="Saturday":
    print("Enter the day:",day)
elif day == "Wednesday":
    print("Enter the day:",day)
else:
    print("Invalid day")

if student == "yes" or student=="no":
    print("Are you a student?",student)
else:
    print("Make sure to enter one of the two answers: yes or no")
print
if day == "Friday" and age > 5:
    Ticketprice += 2

if student == "yes" and age > 5:
    Ticketprice *=0.80
    
if Ticketprice == 0:
    print("Ticket price:Free")
else:
    print(f"Ticket price: ${Ticketprice:.2f}")
