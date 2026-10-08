user_age=int(input("Enter your age: "))

day=input("Enter the day of the week: ")

student=input("Are you a student? (yes/no): ")






if user_age < 5:
    ticket_price = 0

elif user_age <= 12:
    ticket_price = 6

elif user_age <= 59:
    ticket_price = 10

else:
    ticket_price = 7


#check for user age

#Check for Friday discount
if day.lower() == "friday" and ticket_price != 0:
    ticket_price += 2

#Check for student discount
if student.lower() == "yes" and ticket_price != 0:
    ticket_price *= 0.8






#Check for invalid age and day inputs
if user_age < 0:
    print("Invalid age")

    
if day.lower() not in ["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]:
    print("Invalid day")

print("Ticket price: $", round(ticket_price, 2))