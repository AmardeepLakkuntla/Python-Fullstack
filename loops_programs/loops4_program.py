# factorial of a number

num = int(input("enter a number:"))
fact = int(input("enter a factorial number:"))

while num > 0:
    fact = fact * num
    num = num - 1

print("Factorial =", fact)
print("num =", num)
