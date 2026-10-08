age = int(input("inter your age :"))
day = str(input("select the day of trip : "))
stu_or_not = str (input("are you a studint?"))
ticket_price = int(0)
valid_days = ["monday","tuseday","wednesday","friday","saturday","sunday"]

if age < 0:
    print("invalid age")
elif  age < 5:
    ticket_price = 0
    print ("your ticket is free.")

elif 12>=age >=5 :
    ticket_price = 6

elif 59 >= age >=13 :
    ticket_price = 10

else   :
    ticket_price = 7
#_________________________________________________
if day not in valid_days:
    print("invalid day")

if day == "friday" :
    ticket_price = ticket_price + 2

if age>= 5 and stu_or_not == "yes":
    ticket_price=  ticket_price-(ticket_price * 0.20)

print()
print(f"the final ticket price is : ${ticket_price}")


    


 