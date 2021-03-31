print("Wellcome to the Tip Calculator")
bill = input("How much was the total bill? ")
tip = input("What percentage tip would you like to give? 10 or 15 ? ")
people = input("How many people to split the bill? ")
bill_and_tip = float(bill) +  ( float(bill) * float(tip) )/100
result = float(bill_and_tip)/float(people)
result_rounded = round(result, 2 )
print(f"each of you must pay: {result_rounded}$")
