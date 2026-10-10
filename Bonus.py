weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters (e.g., 1.75): "))

bmi = weight / (height ** 2)

print(f"Your BMI is: {bmi:.2f}")

if bmi < 18.5:
    print("You are underweight. Watch your health.")
elif 18.5 <= bmi <= 24.9:
    print("You are fit & healthy.")
else:
    print("You are overweight you need to work out more and watch your diet.")