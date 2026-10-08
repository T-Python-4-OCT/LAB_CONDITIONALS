age = int(input("how old are you")) 
day = input("what day") 
stu = input("Whether they are a student yes or no")
if age < 0: print("Invalid age")
elif age < 5: price = 0
elif age <= 12: price = 6
elif age <= 59: price = 10
else: price = 7
if day not in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]: 
    print("Invalid day")
elif stu not in ["yes", "no"]:
 print("Invalid student")
else: 
    if day == "Friday": price = price + 2 
    if stu == "yes" and price != 0:
     price = price * 0.8 
    
if price == 0:
    print ("Ticket: Free")
else:
    print("Ticket:", price)
