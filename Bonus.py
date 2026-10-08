weight = float(input("Enter your weight (kg): "))
height = float(input("Enter your height (cm): "))

if weight <= 0 or height <= 0:
    print("Invalid input")
else:
    height = height / 100
    bmi = weight / (height ** 2)
    print(f"Your BMI is: {bmi:.1f}")

    if bmi < 18.5:
        print("You are underweight. Watch your health.")
    elif bmi < 25:
        print("You are fit & healthy.")
    else:
        print("You are overweight you need to work out more and watch your diet.")
