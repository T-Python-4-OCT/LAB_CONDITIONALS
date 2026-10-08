
age = int(input("Enter your age:  "))

if age >= 60 :
    price = 7
elif age >=13:
    price = 10
elif age <= 5 :
    price = 0
elif age  <= 12 :
    price = 6

day = str(input("Enter the day:  "))
days = ["Monday"  ,"Tuesday",  "Wednesday",  "Thursday", "Saturday",  "Sunday" ,"Friday"]
price_2 = price
if day == "Friday" and price >0 :
    price_2 = price +2
elif day not in days :
    print("Invalid day")
    exit()

student = str(input("Are you a student?"))
if student.strip() == "yes":
    price_3 = price_2 -(price_2 * 0.20) 
else:
    price_3 = price_2

print("Ticket price:  " +str(price_3)+ " $")





    





    

    

      
