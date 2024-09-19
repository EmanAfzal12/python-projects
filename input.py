num1=int(input("Enter your first number"))
num2=int(input("Enter your second number"))
opt=str(input("""Choose opt
              a.Add
              b.Sub
              c.Mul
              d.div"""))
if opt=="a" or opt =="A":
    print(num1+num2)
elif opt=="b":
    print(num1-num2)
elif opt=="c":
    print(num1*num2)

else:
    print(num1/num2)


    
