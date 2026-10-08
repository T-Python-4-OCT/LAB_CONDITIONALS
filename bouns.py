wieght = int(input("inter your wieght :"))
height = int(input ("inter your height :"))
bmi = (wieght / (height**2)) * 10000
print(bmi)
if bmi <18.5:
    print("You are underweight. Watch your health")

if 24.9 >= bmi >=18.5 :
    print("You are fit & healthy.")

if bmi >= 25 :
    print ("You are overwieght you need to work out more and watch your diet.")