#if and else

score=int(input("score percentage:"))
if (score>=70):
    name=(input("name:"))
    dept=(input("dept:"))
    print("you are eligible")
else:
    print("you are not eligible")
        
#next

salary=int(input("enter your salary:"))
age=int(input("enter your age:"))
if (salary>=20000)or(age<=25):
    loan_amount=int(input("enter your lone amount"))
    if (loan_amount<=50000):
        print("you are eliglble for loan")
    else:
            print("maximum loan amount is 50000")
else:
    print("your not eligible")

