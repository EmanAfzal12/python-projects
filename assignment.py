def calculator():
    while True:
        num1=int(input("Enter  the first number"))
        operator= input("Enter the operator(+, -,,/):")
        num2=int(input("Enter the second number"))

if operator=="+":
    resut=num1+num2
elif operator=="-":
    result=num1-num2
elif operator=="/":
    if num2!=0:
        result=num1/num2
else:
    result="invalid operator, please try again"

if result=="invalid operator, please try again":

    if result>=150:
        print("Total is greater")

else:
    print("Total is smaller")
