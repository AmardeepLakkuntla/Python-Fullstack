def largest(a, b):
    if a > b:
        return a
    else:
        return b
a=int(input("enter first number:"))
b=int(input("enter second number:"))

print("Largest:", largest(a, b))
