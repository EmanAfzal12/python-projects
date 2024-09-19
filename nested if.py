num=int(input("enter your number"))
if num >=18:
    if num >=10:
        print("Hello")
    elif num <=14:
        print("Hey")
else:
    print("Bye")

fruits=["apple","mango", "banana", "orange", "cherry"]
for x in fruits:
    print(x)
for x in fruits:
    if x=="mango":
        continue

A=[1,2,3,4,5,6,7,8]
for y in A:
    print(y)
    if y==6:
        break
a=6
b=8

print("A") if a>b else print("B")

if a>b:
     pass
else:
    print("Not")
    
