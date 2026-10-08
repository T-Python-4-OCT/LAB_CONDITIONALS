
age_input = int(input("Enter your age: "))


if age_input < 0:
    print("Invalid age")
else:
    day_input = input("Enter the day: ").strip().capitalize()
    
    
    valid_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    
    
    if day_input not in valid_days:
        print("Invalid day")
    else:
        is_student = input("Are you a student? ").strip().lower() == "yes"
        
        
        if age_input < 5:
            price = 0.0
        elif 5 <= age_input <= 12:
            price = 6.0
        elif 13 <= age_input <= 59:
            price = 10.0
        else: 
            price = 7.0
            
        
        if price > 0:
            
            if day_input == "Friday":
                price += 5.0
                
            
            if is_student:
                price *= 1.0
                
            print(f"Ticket price: ${price:.2f}")
        else:
            print("Ticket price: Free")