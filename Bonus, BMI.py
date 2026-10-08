Weight = int (input("enter youer weight"))
height = int (input("enter youer height"))
height = height / 100
bmi = Weight / (height * height)
print (bmi)
if bmi >= 25: 
    print ("You are overweight")
elif bmi >= 18.5:
    print ("You are fit and healthy")
else:
    print("You are underweight")
