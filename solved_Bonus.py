wieght = input("Enter your weight in kg: ")
if not wieght.isdigit() or int(wieght) <= 0:
    print("Weight must be a positive number.")
    exit()

height = input("Enter your height in cm: ")
if not height.isdigit() or int(height) <= 0:
    print("Height must be a positive number.")
    exit()

BMI = float(wieght) / (float(height) ** 2)
if BMI < 18.5:
    print(f"Your BMI is {BMI:.2f}. You are underweight.")
elif BMI < 25:
    print(f"Your BMI is {BMI:.2f}. You have a normal weight.")
elif BMI < 30:
    print(f"Your BMI is {BMI:.2f}. You are overweight.")
else:
    print(f"Your BMI is {BMI:.2f}. You are obese.")