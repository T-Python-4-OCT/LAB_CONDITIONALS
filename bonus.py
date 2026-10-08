weight = float(input("Please enter your weight in kg: "))
height = float(input("Please enter your height in cm: "))/100

if height <= 0 or weight <= 0:
    print("Invalid height or weight.")

else:
    bmi = weight / (height ** 2)
    print(f"Your BMI is: {bmi}")

    if bmi < 18.5:
        print("You are underweight.")
    elif bmi < 25:
        print("You have a normal weight.")
    elif bmi < 30:
        print("You are overweight.")
    else:
        print("You are obese.")