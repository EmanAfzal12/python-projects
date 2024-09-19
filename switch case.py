Traffic=str(input("enter your color Red, Yellow, Green"))
match Traffic:
    case "Red":
        print ("stop")
    case "Yellow":
        print ("Ready")
    case "Green":
        print ("Go")

A= int(input("enter your number"))
match A:
    case 1:
        print ("One")
    case 2:
        print ("Two")
    case default:
        print("Try again")

num=int(input("enter your number"))
if num%2==0:
    print("The value is Even")
else:
    print("The value is odd")

a=int(input("enter your number"))
if a<0:
    print("Negative")
else:
    print("Positive")
    
