
a= int(input("Enter your number"))

if a<0:
    print("Negative")

else:
    print("Positive")

Name=str(input("Enter your name"))
English=int(input("Enter english marks:"))
Urdu=int(input("Enter Urdu marks:"))
Maths=int(input("Enter Maths marks:"))
Science=int(input("Enter Science marks:"))
Sst=int(input("Enter Social studies marks:"))

add=(English+Urdu+Maths+Science+Sst)
per=add/500*100
print=("Total",per,"%")
