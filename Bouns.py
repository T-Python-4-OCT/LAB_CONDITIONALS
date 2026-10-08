heigth = float(input("Enter your heigth: "))
weight = float(input("Enter your weight: "))
bmi = weight / ((heigth / 100 )** 2 )

if bmi <18.5 : 
    print("Underweight , you need to eat more !")
elif bmi < 25:
    print("Normal , keep it up !")
elif bmi < 30:
    print("Overweight , you need to exercise more !")
else:
    print("Obese")


print("Your BMI is", bmi)


#output : 
# Enter your heigth: 176
# Enter your weight: 87
# Overweight , you need to exercise more !
# Your BMI is 28.08626033057851