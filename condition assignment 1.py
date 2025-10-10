
    
temp=float(input("enter the temperature: "))
text=input("is the temp in celcius or fahrenheit? (C/F): ")
if text=="C":
    fahrenheit=(temp*9/5)+32
    print("temp in fahrenheit:",fahrenheit)
elif text=="F":
    Celsius=(temp-32)*5/9
    print("temp in Celsius:",Celsius)
else:
    print("invalid text:please enter 'C' for celsius or 'F' for fahrenheit.")


temp=float(input("enter the temperature: "))
text=input("is the temp in celcius or fahrenheit? (C/F): ")
if text=="C":
    converted=(temp*9/5)+32
    print(f"{temp}is equal to {converted:.2f} F.")
elif text=="F":
    converted=(temp-32)*5/9
    print(f"{temp}is equal to {converted:.2f} C.")
else:
    print("invalid text:please enter 'C' for celsius or 'F' for fahrenheit.")