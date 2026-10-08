weight=int(input("Enter your weight in kg: "))
height=int(input("Enter your height in cm: "))
height=height/100
mass= weight/(height**2)

print(f"Your BMI is: {mass:.2f}")
if mass<18.5:
    print("You are underweight.")
elif mass<24.9:
    print("You have a normal weight.")
elif mass<29.9:
    print("You are overweight.")
else:
    print("You are obese.")
