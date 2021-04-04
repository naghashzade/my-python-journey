print("Wellcome to the Rollercoaster.")
if int(input("Height in cm: ")) >= 120:
    age = int(input("Age: "))
    if age >= 18:
        print("your ticket costs 7$")
    elif age < 12:
        print("your ticket costs 3$")
    else:
        print("your ticket costs 5$")
else:
    print("you are not allowed to use rollercoaster.")