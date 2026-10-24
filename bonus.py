# مؤشر كتلة الجسم = الوزن بالكيلوجرام ÷ مربع الطول 

weight = float(input("Weight in kg: "))
height = float(input("Height in cm: ")) / 100
bmi = weight / (height ** 2)

print(f"BMI: {bmi:.2f}")

if bmi >= 25:
    print("You are overweight. Work out more and watch your diet.")
elif bmi >= 18.5:
    print("You are fit & healthy.")
else:
    print("You are underweight. Watch your health.")
