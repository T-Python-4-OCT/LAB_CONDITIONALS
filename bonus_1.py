
weight= float(input("Enter your weight in  : kg    "))
height = float(input("Enter your height in  : cm   "))
height_1 = height / 100
bmi = weight / (height_1 *  height_1) 
print(round(bmi) ,1)

if bmi <= 18.5 :
    print("You are underweight. Watch your health.")
elif bmi <=24.9 :
    print("You are fit & healthy.")
elif bmi >=25:
    print("You are overwieght you need to work out more and watch your diet.")