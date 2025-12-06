# printing even numbers

a=int(input("enter first number: "))
b=int(input("enter the second number: "))

for i in range(a, b):
    if i % 2 == 0:
        print(i)
