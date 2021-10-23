#1
salary=float(input("entre the user's salary:"))
year=int(input("entre the year the user has been working on:"))
flag=False
if year>5:
    updated_salary=salary*0.05
    increased_salary=salary+updated_salary
    print("his new salary is:",increased_salary)
    flag=True

else:
    flag=False
    print("he did not do 5 years because he is noob",salary)