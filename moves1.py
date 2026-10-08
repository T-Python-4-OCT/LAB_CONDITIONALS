

print("Welcome to the moves! Let's get started.")

price:int= 10
age = int(input("Please enter your age: "))
day_of_week = input("What day of the week is it? ").lower()
student_status = input("Are you a student? (yes/no): ").lower()



if day_of_week == "saturday" or day_of_week == "sunday" or day_of_week == "monday"or day_of_week == "tuesday" or day_of_week == "wednesday" or day_of_week == "thursday":
    price += 0
elif day_of_week == "friday":
    price += 2
else:
    print("Invalid day of the week.")
    


if age<5:
    price*=0
elif age<13:
    price-=4
elif age<60:
    price+=0
elif age<120:
    price-=3
elif age<0:
    print("Invalid age. Please enter a valid age.")
else:
    print("Invalid age. Please enter a valid age.")
    
    
    
if student_status=="yes":
    price*=0.8
    
else:
    price+=0



if price==0:
    print("The final price is: Free")
else:
    print(f"The final price is: ${price:.2f}")

