#Convert A Temperature Celsius to fahrenheit# 
def celsius_to_Fahrenheit(Celsius):
    return(Celsius*9/5)+32
#test Function#
Celsius=float(input("enter temperature in Celsius"))
Fahrenheit=celsius_to_Fahrenheit(Celsius)
print(f"{Celsius}C is equal to{Fahrenheit}F")
