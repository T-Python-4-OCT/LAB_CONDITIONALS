# LAB_CONDITIONALS

age:int = int(input("Enter your Age: "))
day:str = input("Enter the day: ")
studens:bool = input("Are you a student?")




ticket_price:int = 0
extra_price:int = 2
offStudent:int = 20 / 100


if day != "Monday" and day != "Tuesday" and day != "Wednesday" and day != "Thursday" and day != "Friday" and day != "Saturday" and day != "Sunday":
       print("Invalid day")
       if age < 0:
        print("Invalid age")
elif age < 5:
    ticket_price = 0
elif age >= 5 and age <= 12:
    ticket_price = 6
    if day == "Friday":
        ticket_price = ticket_price + extra_price
    if studens == "yes":
         ticket_price = ticket_price * (1 - offStudent)
elif age >= 13 and age <= 59:
    ticket_price = 10
    if day == "Friday":
            ticket_price = ticket_price + extra_price
    if studens == "yes":
             ticket_price = ticket_price * (1 - offStudent)
elif age >= 60:
     ticket_price = 7
     if day == "Friday":
                 ticket_price = ticket_price + extra_price
     if studens == "yes":
                  ticket_price = ticket_price * (1 - offStudent)

if ticket_price == 0:
    print("Ticket price: Free")
elif ticket_price == 0:
    print("Ticket price: Free")
else:
    print("Ticket price: $" + format(round(ticket_price, 2), ".2f"))
        


    

