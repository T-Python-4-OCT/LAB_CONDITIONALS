age =int(input("Enter your age: "))
day = input("Enter the day : ").lower()
student = input("Are you student?: ").lower()
price = 0
print("invalid age")

if age < 5:
   price = 0
elif age <= 12: 
    price = 6
elif age <= 59:
    price = 10

if day =="sunday"or day == "monday" or day == "tuseday" or day == "wednnesday" or day== "thusday" or day =="saturday":

    price+=0

elif day == "friday":
    price +=2
else:
    print("invalid day")



if student== "yes":
    price *= 0.8
elif student == "no":
    price *= 1

print(f"The ticket price is: ${price:.2f}")