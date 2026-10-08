weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters : "))

bmi = weight / (height**2)

print("Your BMI is:", round(bmi, 2))

if bmi < 18.5:
    print("You are underweight. Watch your health.")
elif bmi <= 24.9:
    print("You are fit & healthy.")
else:
    print("You are over weight you need to work out more and watch your diet.")