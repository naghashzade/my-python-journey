age = input("Insert your age: ")
age_to_month = int(age) * 12 
age_to_week = int(age) * 52
age_to_day = int(age) * 365
remain_year = 90 - int(age)
remain_month = 90*12 - int(age_to_month)
remain_week = 90*52 - int(age_to_week)
remain_day = 90*365 - int(age_to_day)
print(f"you will live {remain_year} years and {remain_month} months and {remain_week} weeks and {remain_day}")
print("if you are lucky enough to live 90 years")
