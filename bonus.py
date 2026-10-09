# Bouns

wieght = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in m: "))


ibm = wieght / (height ** 2)

if ibm >= 25:
    print("You are overwieght you need to work out more and watch your diet.")
elif ibm >= 18.5:
    print("You are fit & healthy.")   
else:
    print("You are underweight. Watch your health.")
