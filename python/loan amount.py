salary=int(input("enter the sal:"))
age=int(input("enter the age:"))
if(salary>=20000 or age <=25):
    loan = int(input("enter the loan:"))
    if(loan>50000):
        print("min loan is 50000")
    else:
        print("you'r elgible for loan")
else:
    print("you'r not elgible for loan")
