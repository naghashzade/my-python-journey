# bmi calc ver 2 
print("Wellcome to BMI Calculator")
height_cm = int(input("Height in cm: "))
weight = int(input("Weight in Kg: "))
height_m = height_cm / 100
bmi = round(weight / (height_m)**2 , 2)
if bmi >= 30:
    print(f"Your BMI is {bmi} and you are Obese ")
elif bmi >= 25:
    print(f"Your BMI is {bmi} and you are Overweight ")
elif bmi >= 18.5:
    print(f"Your BMI is {bmi} and you are Normal weight ")
else:
    print(f"Your BMI is {bmi} and you are Underweight ")